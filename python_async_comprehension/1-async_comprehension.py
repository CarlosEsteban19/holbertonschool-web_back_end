#!/usr/bin/env python3
"""1-async_comprehension.py"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """1-async_comprehension.py"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
