#!/usr/bin/env python
"""
Python library to manipulate Jinja-template DMC files
"""
# SPDX-License-Identifier: LGPL-3.0
#
# Author: Dean Serenevy  <dean@serenevy.net>
# This software is Copyright (c) 2017 Dean Serenevy.
# This software is Copyright (c) 2013 APCI, LLC.

import re

__version__ = re.search(r'(?m)^__version__\s*=\s*"([\d.]+(?:[\-\+~.]\w+)*)"', open('dmctool/__init__.py').read()).group(1)

from setuptools import setup

import unittest
def my_test_suite():
    return unittest.TestLoader().discover('test', pattern='test_*.py')

setup(
    name         = 'dmctool',
    version      = __version__,
    author       = "Dean Serenevy",
    author_email = 'dean@serenevy.net',
    description  = "Python library to manipulate Jinja-template DMC files",
    packages     = [ 'dmctool' ],
    scripts      = [ 'bin/dmctool' ],
    provides     = "dmctool",
    requires     = [ "jinja2_apci", ],
    test_suite   = 'setup.my_test_suite',
)
