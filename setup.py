#!/usr/bin/env python
"""
Python library to manipulate Jinja-template DMC files
"""
# Author: Dean Serenevy  <dean@serenevy.net>
# This software is Copyright (c) 2017 Dean Serenevy.
# This software is Copyright (c) 2013 APCI, LLC.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
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
