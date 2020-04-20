import ssl

from aiogremlin.driver import pool


class GremlinServer:
    """
    Class that wraps a connection pool. Currently doesn't do much, but may
    be useful in the future....

    :param pool.ConnectionPool pool:
    """

    def __init__(self, url, loop, **config):
        self._pool = None
        self._url = url
        self._loop = loop
        self._response_timeout = config['response_timeout']
        self._username = config['username']
        self._password = config['password']
        self._max_times_acquired = config['max_times_acquired']
        self._max_conns = config['max_conns']
        self._min_conns = config['min_conns']
        self._max_inflight = config['max_inflight']
        self._message_serializer = config['message_serializer']
        self._provider = config['provider']
        scheme = config['scheme']
        if scheme in ['https', 'wss']:
            certfile = config['ssl_certfile']
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            ssl_context.load_verify_locations(cafile=certfile)
            self._ssl_context = ssl_context
        else:
            self._ssl_context = None

    @property
    def url(self):
        return self._url

    @property
    def pool(self):
        """
        Readonly property.

        :returns: :py:class:`ConnectionPool<aiogremlin.driver.pool.ConnectionPool>`
        """
        if self._pool:
            return self._pool

    async def close(self):
        """**coroutine** Close underlying connection pool."""
        if self._pool:
            await self._pool.close()
            self._pool = None

    async def get_connection(self):
        """**coroutine** Acquire a connection from the pool."""
        try:
            conn = await self._pool.acquire()
        except AttributeError:
            raise Exception("Please initialize pool")
        return conn

    async def initialize(self):
        conn_pool = pool.ConnectionPool(
            self._url, self._loop, self._ssl_context, self._username,
            self._password, self._max_conns, self._min_conns,
            self._max_times_acquired, self._max_inflight,
            self._response_timeout, self._message_serializer, self._provider)
        await conn_pool.init_pool()
        self._pool = conn_pool

    @classmethod
    async def open(cls, url, loop, **config):
        """
        **coroutine** Establish connection pool and host to Gremlin Server.

        :param str url: url for host Gremlin Server
        :param asyncio.BaseEventLoop loop:
        :param ssl.SSLContext ssl_context:
        :param str username: Username for database auth
        :param str password: Password for database auth
        :param float response_timeout: (optional) `None` by default
        :param int max_conns: Maximum number of conns to a host
        :param int min_connsd: Minimum number of conns to a host
        :param int max_times_acquired: Maximum number of times a conn can be
            shared by multiple coroutines (clients)
        :param int max_inflight: Maximum number of unprocessed requests at any
            one time on the connection

        :returns: :py:class:`GremlinServer`
        """

        host = cls(url, loop, **config)
        await host.initialize()
        return host
