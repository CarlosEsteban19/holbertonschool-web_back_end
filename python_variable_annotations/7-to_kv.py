#!/usr/bin/env python3
"""mi codigo se ve bn"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """tuple y su madre"""
    result: float = v * v
    return tuple(k, result)
