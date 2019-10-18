#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0
#
# Author: Dean Serenevy  <dean@serenevy.net>
# This software is Copyright (c) 2017 Dean Serenevy.
# This software is Copyright (c) 2013 APCI, LLC.

from __future__ import division, absolute_import, print_function, unicode_literals
import unittest

import datetime
import os.path
import sys
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmctool.util import dmcadd_xAPI, string_to_galil_hex, galil_hex_to_string, galil_hex_to_binary

class TestUtil(unittest.TestCase):

    def test_xapi(self):
        timestamp = datetime.datetime.today()
        self.assertEqual(
            dmcadd_xAPI("#xINIT;EN\n#xAPIOk;EN\n", "foo", "12345", columns=79),
            timestamp.strftime("""
#xINIT;xPrgName="foo";xPrgHash=12345;xAPIOk=0;xPrgDate=%Y%m%d;EN
#xAPIOk;xAPIOk=xAPIOk+1;EN
""".lstrip()))

    def test_strings(self):
        self.assertEqual(string_to_galil_hex('12345'), '$31323334.3500')
        self.assertEqual(galil_hex_to_string('$31323334.3500'), '12345')
        self.assertEqual(galil_hex_to_binary('$31323334.3500'), '12345\x00')


if __name__ == '__main__':
    unittest.main()
