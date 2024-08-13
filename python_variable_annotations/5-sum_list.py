#!/usr/bin/env python3
"""sum list of stuff"""
from typing import List


def sum_list(imput_list: List[float]) -> float:
    """hola mami"""
    result: float = 0
    for num in imput_list:
        result += num
    return result
