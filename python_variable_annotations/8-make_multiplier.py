#!/usr/bin/env python3
"""codigo G - Eladio"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """comentando esto tambn"""

    def funcion(x: float) -> float:
        """por si las moscas"""
        return x * multiplier

    return funcion
