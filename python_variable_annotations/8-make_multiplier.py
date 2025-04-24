#!/usr/bin/env python3
"""
takes a float multiplier as argument
returns a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplier: float) -> callable:
    '''Creating a multiplier function'''
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
