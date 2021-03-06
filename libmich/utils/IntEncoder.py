# -*- coding: UTF-8 -*-
#/**
# * Software Name : libmich 
# * Version : 0.2.3
# *
# * Copyright © 2014. Benoit Michau. ANSSI.
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License version 2 as published
# * by the Free Software Foundation. 
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details. 
# *
# * You will find a copy of the terms and conditions of the GNU General Public
# * License version 2 in the "license.txt" file or
# * see http://www.gnu.org/licenses/ or write to the Free Software Foundation,
# * Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
# *
# *--------------------------------------------------------
# * File Name : utils/IntEncoder.py
# * Created : 2014-06-17
# * Authors : Benoit Michau 
# *--------------------------------------------------------
#*/ 
#!/usr/bin/env python

###
# provides minimum encoding for signed integer
###
def minenc_int(val=0):
    '''
    for a given signed integer value, returns the minimum octet encoding,
    limited to 8 bytes (int64).
    
    minenc_int(X) -> (Y, 'intZ')
        1 <= Y <= 8
        'int8' -> 'int64'
    '''
    if -128 <= val < 128:
        return (1, 'int8')
    elif -32768 <= val < 32768:
        return (2, 'int16')
    elif -8388608 <= val < 8388608:
        return (3, 'int24')
    elif -2147483648 <= val < 2147483648:
        return (4, 'int32')
    elif -549755813888 <= val < 549755813888:
        return (5, 'int40')
    elif -140737488355328 <= val < 140737488355328:
        return (6, 'int48')
    elif -36028797018963968 <= val < 36028797018963968:
        return (7, 'int56')
    elif -9223372036854775808 <= val < 9223372036854775808:
        return (8, 'int64')
    else:
        return (0, None)

###
# provides minimum encoding for unsigned integer
###
def minenc_uint(val=0):
    '''
    for a given unsigned integer value, returns the minimum octet encoding,
    limited to 8 bytes (uint64).
    
    minenc_uint(X) -> (Y, 'intZ')
        1 <= Y <= 8
        'uint8' -> 'uint64'
    '''
    if 0 <= val < 256:
        return (1, 'uint8')
    elif 0 <= val < 65536:
        return (2, 'uint16')
    elif 0 <= val < 16777216:
        return (3, 'uint24')
    elif 0 <= val < 4294967296:
        return (4, 'uint32')
    elif 0 <= val < 1099511627776:
        return (5, 'uint40')
    elif 0 <= val < 281474976710656:
        return (6, 'uint48')
    elif 0 <= val < 72057594037927936:
        return (7, 'uint56')
    elif -9223372036854775808 <= val < 9223372036854775808:
        return (8, 'uint64')
    else:
        return (0, None)

