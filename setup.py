#!/usr/bin/env python
'''
    This file is part of python-webuntis

    :copyright: (c) 2012 by Markus Unterwaditzer.
    :license: BSD, see LICENSE for more details.
'''

from setuptools import setup, find_packages
from sys import version_info
import pkg_resources

dependencies = []

if version_info < (2,6):
    dependencies.append('simplejson')

if version_info < (2,7):
    dependencies.append('ordereddict')

setup(
    name='webuntis',
    version='0.1.4',
    author='Markus Unterwaditzer',
    author_email='markus@unterwaditzer.net',
    packages=['webuntis', 'webuntis.utils', 'webuntis.tests'],
    include_package_data=True,
    url='http://dev.unterwaditzer.net/python-webuntis/',
    license='new-style BSD',
    description='Bindings for WebUntis API',
    long_description=open('README.rst').read(),
    install_requires=dependencies,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    test_suite='webuntis.tests'
)
