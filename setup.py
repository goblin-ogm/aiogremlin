import pip
from setuptools import setup

__author__ = 'Jeffrey Phillips Freeman'
__email__ = 'Jeffrey.Freeman@CleverThis.com'
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2017, CleverThis, Inc. and contributors'
__credits__ = ['David M. Brown - Project founder']

setup(
    name='aiogremlin',
    version='3.3.2',
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='An asynchronous DSL for the Gremlin-Python driver',
    long_description='This project is officially hosted on QOTO GitLab here: https://git.qoto.org/goblin-ogm/aiogremlin',
    url='https://git.qoto.org/goblin-ogm/aiogremlin',
    download_url='https://github.com/goblin-ogm/aiogremlin/archive/v3.3.2.tar.gz',
    include_package_data=True,
    keywords=['Tinkerpop', 'Tinkerpop3', 'gremlin', 'gremlin-python', 'asyncio', 'graphdb'],
    packages=['aiogremlin',
              'aiogremlin.driver',
              'aiogremlin.driver.aiohttp',
              'aiogremlin.process',
              'aiogremlin.structure',
              'aiogremlin.remote'],
    install_requires=[
        'gremlinpython<=3.4.3',
        'aenum>=1.4.5',  # required gremlinpython dep
        'aiohttp>=2.2.5',
        'PyYAML>=3.12',
        'six>=1.10.0'  # required gremlinpython dep
    ],
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['pytest-asyncio', 'pytest-timeout', 'pytest', 'mock'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
