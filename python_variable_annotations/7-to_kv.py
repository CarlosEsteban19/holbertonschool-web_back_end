#!/usr/bin/env python3
"""mi codigo se ve bn"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """tuple y su madre"""
    result: float = v * v
    return (k, result)
