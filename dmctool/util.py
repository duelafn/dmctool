# -*- coding: utf-8 -*-
"""

"""
# SPDX-License-Identifier: LGPL-3.0
#
# Author: Dean Serenevy  <dean@serenevy.net>
# This software is Copyright (c) 2017 Dean Serenevy.
# This software is Copyright (c) 2013 APCI, LLC.
from __future__ import division, absolute_import, print_function, unicode_literals
__all__ = '''
dmcadd_xAPI
dmchash
dmcround
galil_hex_to_binary
galil_hex_to_string
string_to_galil_hex
'''.split()


import hashlib
from binascii import b2a_hex


def string_to_galil_hex(string):
    """
    On a Galil board, even strings are stored in Galil4,2 format. This
    method will return a hex string as Galil would store the string.

    E.g.: '12345' -> '$31323334.3500'
    """
    if (len(string) > 6):
        raise ValueError("Galil strings may have at most 6 characters")
    hexstring = b2a_hex(string.encode('utf-8').ljust(6, b"\0")).decode('utf-8')
    return ('$' + hexstring[0:8] + '.' + hexstring[8:12]).upper()

def galil_hex_to_string(ghex):
    """
    On a Galil board, even strings are stored in Galil4,2 format. This
    method will return a readable string from a Galil hex string.

    E.g.: '$31323334.3500' -> '12345'
    """
    return re.sub('[a-zA-Z0-9]{2}', hex2str, ghex.translate(None, '$.')).rstrip("\0")

def galil_hex_to_binary(ghex):
    """
    Just like galil_hex_to_string but does not strip trailing null bytes.

    E.g.: '$31323334.3500' -> '12345\\x00'
    """
    return re.sub('[a-zA-Z0-9]{2}', hex2str, ghex.translate(None, '$.'))

def dmchash(program):
    """
    Computes a hash of the program. Returns a Galil string.
    """
    m = hashlib.md5()
    m.update(program.encode('utf-8'))
    return string_to_galil_hex(m.hexdigest()[0:6])

def dmcround(val):
    """
    Rounds a value to galil precision. If the value then is an
    integral value, will return a python int so that its
    stringification is correct.
    """
    val = round(float(val), 4)
    return int(val) if val == int(val) else val

def dmcadd_xAPI(program, name, hash, columns=79):
    """
    Returns a modified program with required xAPI support functions.

    Replaces any empty #xINIT and #xAPIOk functions (must be only thing
    on line) in the program with correct implementations which set the
    program name/hash and which implement the xAPI verification.

    This action WILL change the length of the lines defining these
    functions so the functions definitions should be the only thing on
    the line. (shouldn't be a problem since any otimizer will leave the
    #XXXX at the beginning of a line).

    if columns are too small, this function WILL modify the line count
    in order to satisfy the column requirements. Otherwise it will not.
    """
    xINIT = '#xINIT;xPrgName="{}";xPrgHash={};xAPIOk=0;EN\n'.format(name, hash)
    if columns < len(xINIT):
        xINIT = '#xINIT;xPrgName="{}";\nxPrgHash={};\nxAPIOk=0;EN\n'.format(name, hash)

    return program.replace(
        "#xINIT;EN\n", xINIT
    ).replace(
        "#xAPIOk;EN\n", '#xAPIOk;xAPIOk=xAPIOk+1;EN\n'
    )
