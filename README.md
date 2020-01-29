# [aiogremlin](https://pypi.python.org/pypi/aiogremlin/3.2.4)
[![tests](http://git.qoto.org/goblin-ogm/aiogremlin/badges/master/pipeline.svg)](http://git.qoto.org/goblin-ogm/aiogremlin/commits/master)
[![test coverage](http://git.qoto.org/goblin-ogm/aiogremlin/badges/master/coverage.svg)](http://git.qoto.org/goblin-ogm/aiogremlin/commits/master)
[![Requirements](https://requires.io/github/goblin-ogm/aiogremlin/requirements.svg?branch=master)](https://requires.io/github/goblin-ogm/aiogremlin/requirements/?branch=master)
[![Gitter](https://badges.gitter.im/Syncleus/aparapi.svg)](https://gitter.im/Syncleus/aparapi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![PyPi](https://img.shields.io/pypi/v/aiogremlin.svg?style=flat)](https://pypi.python.org/pypi/aiogremlin)
[![Downloads](https://img.shields.io/pypi/dm/aiogremlin.svg?style=flat)](https://pypi.python.org/pypi/aiogremlin)
[![SemVer](https://img.shields.io/badge/SemVer-v2.0.0-green)](https://semver.org/spec/v2.0.0.html)
[![docs](https://readthedocs.org/projects/aiogremlin/badge/?version=latest)](https://aiogremlin.readthedocs.io/en/latest/)

[Official Documentation](http://aiogremlin.readthedocs.org/en/latest/)

`aiogremlin` is an asynchronous DSL based on the official `Gremlin-Python` GLV designed for integration with
event loop based asynchronous Python networking libraries, including `asyncio`,
`aiohttp`, and `tornado`. It uses the `async/await` syntax introduced
in PEP 492, and is therefore Python 3.5+ only.

`aiogremlin` tries to follow `Gremlin-Python` as closely as possible both in terms
of API and implementation. It is released according to the TinkerPop release schedule.

Note that this *NOT* an official Apache project component, it is a
*THIRD PARTY PACKAGE!*

## Getting Started

```python
import asyncio
from aiogremlin import DriverRemoteConnection, Graph


loop = asyncio.get_event_loop()


async def go(loop):
  remote_connection = await DriverRemoteConnection.open(
    'ws://localhost:8182/gremlin', 'g')
  g = Graph().traversal().withRemote(remote_connection)
  vertices = await g.V().toList()
  await remote_connection.close()
  return vertices


vertices = loop.run_until_complete(go(loop))
print(vertices)
# [v[1], v[2], v[3], v[4], v[5], v[6]]
```

## Developers

### Testing

In order to perform tests identical in nature to the integration tests we run then simply ensure you gave gitlab-runner installed then run the following command.

```bash
gitlab-runner exec docker test
```

Keep in mind this will run the tests on your local copy of the master branch so any changes not committed locally will be missed when testing.
