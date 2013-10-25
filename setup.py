# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages


_version = "0.1"
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "pylint-celery is a Pylint plugin to aid Pylint in recognising and understanding" \
                     "errors caused when using the Celery library"


setup( name='pylint-celery',
       url='https://github.com/landscapeio/pylint-celery',
       author='landscape.io',
       author_email='code@landscape.io',
       description=_short_description,
       version=_version,
       packages=_packages,
       install_requires=['pylint', 'astroid', 'pylint-plugin-utils'],
       license='GPLv2',
       keywords='pylint celery plugin'
)
