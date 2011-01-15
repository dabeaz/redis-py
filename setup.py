#!/usr/bin/env python
from redis import __version__

sdict = {
    'name' : 'redis',
    'version' : __version__,
    'description' : 'Python 3 client for Redis key-value store',
    'long_description' : 'Python 3 client for Redis key-value store',
    'url': 'http://github.com/dabeaz/redis-py',
    'author' : 'Andy McCurdy',
    'author_email' : 'sedrik@gmail.com',
    'maintainer' : 'David Beazley',
    'maintainer_email' : 'dave@dabeaz.com',
    'keywords' : ['Redis', 'key-value store'],
    'license' : 'MIT',
    'packages' : ['redis'],
    'test_suite' : 'tests.all_tests',
    'classifiers' : [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(**sdict)

