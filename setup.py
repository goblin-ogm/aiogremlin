import pip
from setuptools import setup


setup(
    name='aiogremlin',
    version='3.3.2',
    url='',
    license='Apache Software License',
    author='Jeffrey Phillips Freeman',
    author_email='Jeffrey.Freeman@CleverThis.com',
    description='Async Gremlin-Python',
    long_description=open('README.md').read(),
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
        'Programming Language :: Python :: 3.5'
    ]
)
