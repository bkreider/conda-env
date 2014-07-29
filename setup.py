#!/usr/bin/env python
# (c) 2014 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda-env is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

import sys
import os

import versioneer

try:
    from setuptools import setup
    using_setuptools = True
except ImportError:
    from distutils.core import setup
    using_setuptools = False

if sys.version_info[:2] < (2, 7) or sys.version_info > (3, 0) and sys.version_info < (3, 3):
    sys.exit("conda-env is only meant for Python 2.7 or 3.3 and up. current version: %d.%d" % sys.version_info[:2])

versioneer.versionfile_source = 'conda_env/_version.py'
versioneer.versionfile_build = 'conda_env/_version.py'
versioneer.tag_prefix = '' # tags are like 1.2.0
versioneer.parentdir_prefix = 'conda-env-' # dirname like 'myproject-1.2.0'

setup(
    name = "conda-env",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author = "Continuum Analytics, Inc.",
    author_email = "ilan@continuum.io",
    url = "https://github.com/conda/conda-env",
    license = "BSD",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    description = "package management tool",
    long_description = open('README.rst').read(),
    packages = ['conda_env'],
    scripts = [
        'bin/conda-env',
    ],
    install_requires = ['conda-api'],
)
