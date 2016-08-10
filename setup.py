#!/usr/bin/env python

from __future__ import with_statement

import os.path

from setuptools import setup


def read(filename):
    """Read files relative to this file."""
    full_path = os.path.join(os.path.dirname(__file__), filename)
    with open(full_path, 'r') as fh:
        return fh.read()


setup(
    name='uwhoisd-redis-cache',
    version='0.0.1',
    description="Redis cache plugin for uwhoisd",
    long_description=read('README') + "\n\n" + read("ChangeLog"),
    url='https://github.com/kgaughan/uwhoisd-redis-cache/',
    license='MIT',
    py_modules=['uwhoisd_rediscache'],
    zip_safe=True,

    setup_requires=[
        'setuptools',
        'wheel',
    ],
    install_requires=[
        'uwhoisd',
        'redis'
    ],

    entry_points={
        'uwhoisd.cache': (
            'redis = uwhoisd_rediscache:Redis',
        ),
    },

    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: System :: Networking',
    ),

    author='Keith Gaughan',
    author_email='k@stereochro.me',
)
