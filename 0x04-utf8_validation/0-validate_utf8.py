#!/usr/bin/python3
"""UTF-8 Validation"""

def count_bit(data):
    """count bits in one data"""
    nb = 0
    rm = 1 << 7
    while rm & data:
        nb += 1
        rm >>= 1
    return nb


def validUTF8(data):
    """validation"""
    nb = 0
    for i in range(len(data)):
        if nb == 0:
            nb = count_bit(data[i])
            if nb == 0:
                continue
            if nb == 1 or nb > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        nb -= 1
    return nb == 0
