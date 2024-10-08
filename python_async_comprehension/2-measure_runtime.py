#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """2-measure_runtime.py"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension())
    end = time.perf_counter()
    total = end - start
    return total
