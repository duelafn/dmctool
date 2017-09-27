#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from __future__ import division, absolute_import, print_function, unicode_literals
import unittest

import sys
import json
from os.path import join, isdir

from subprocess import call

from dmctool import GalilFile
from jinja2 import UndefinedError

class BasicAccess(unittest.TestCase):
    def d(self, *paths):
        return join(self.testdir, *paths)

    def setUp(self):
        self.testdir = "test" if isdir("test") else "."

        self.gf = GalilFile(path=self.d("gal"))
        with open(self.d("machine.json"),'r') as fh:
            self.machine = json.load(fh)

    def test_galtest(self):
        got = self.gf.load("galtest.gal", self.machine)
        with open(self.d('gal/galtest.out')) as fh:
            wanted = fh.read().strip()
        self.assertEqual( got, wanted, "galtest.gal" )

        with self.assertRaises(UndefinedError):
            self.gf.load("galtest.gal", dict())


if __name__ == '__main__':
    unittest.main()
