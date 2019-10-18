#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0
#
# Author: Dean Serenevy  <dean@serenevy.net>
# This software is Copyright (c) 2017 Dean Serenevy.
# This software is Copyright (c) 2013 APCI, LLC.

from __future__ import division, absolute_import, print_function, unicode_literals
import unittest

import sys
import json
import os.path
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmctool.file import GalilFile
from jinja2 import UndefinedError

class BasicAccess(unittest.TestCase):
    testdir = "test" if os.path.isdir("test") else "."

    def d(self, *paths):
        return os.path.join(self.testdir, *paths)
    def read(self, *paths):
        with open(self.d(*paths), 'r') as fh:
            return fh.read()

    def test_basic(self):
        gf = GalilFile(path=self.d("gal"))
        machine = json.loads(self.read("machine.json"))
        wanted = self.read('gal/galtest.out').strip()

        got = gf.load("galtest.gal", machine)
        self.assertEqual( got, wanted, "galtest.gal" )

        with self.assertRaises(UndefinedError):
            gf.load("galtest.gal", dict())

    def test_load_str(self):
        gf = GalilFile()
        machine = json.loads(self.read("machine.json"))
        wanted = self.read('gal/galtest.out').strip()
        source = self.read('gal/galtest.gal').strip()

        got = gf.load_str(source, machine)
        self.assertEqual( got, wanted )


if __name__ == '__main__':
    unittest.main()
