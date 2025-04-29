#!/usr/bin/env python3
"""
write a coroutine called async_comprehension that takes no arguments.
"""
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Collects 10 random numbers using async comprehension."""
    return [i async for i in async_generator()]
