#!/usr/bin/env python3
"""
takes a float multiplier as argument
returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creating a multiplier function'''
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
