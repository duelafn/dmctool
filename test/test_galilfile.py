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

from subprocess import call

from dmctool.file import GalilFile
from jinja2 import UndefinedError

class BasicAccess(unittest.TestCase):
    def d(self, *paths):
        return os.path.join(self.testdir, *paths)

    def setUp(self):
        self.testdir = "test" if os.path.isdir("test") else "."

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
