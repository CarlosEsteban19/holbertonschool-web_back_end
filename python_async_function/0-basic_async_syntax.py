#!/usr/bin/env python3
"""comentandoooooo"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """otro comentariooo"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
