#!/usr/bin/env python3
"""comentandoooooo"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """otro comentario"""
    delays = []

    # CORRE WAIT_RANDOM N VECES
    for x in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    # SORT SIN SORT()
    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key

    return delays
