#!/usr/bin/env python3

import asyncio
import time
import typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of 4 parallel comprehensions."""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
