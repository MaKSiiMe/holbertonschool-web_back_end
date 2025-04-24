#!/usr/bin/env python3
"""
takes a float n as argument
returns the floor of the float.
"""


def floor(n: float) -> int:
    '''Returning the floor of a float'''
    return int(n) if n >= 0 else int(n) - 1
