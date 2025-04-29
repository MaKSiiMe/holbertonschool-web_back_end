#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Yields a random number between 0 and 10 every second, 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
