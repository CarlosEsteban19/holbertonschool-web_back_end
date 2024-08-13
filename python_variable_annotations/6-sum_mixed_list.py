#!/usr/bin/env python3
"""documentando codigo"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """funcion q hace algo"""
    result: float = 0
    for num in mxd_lst:
        result += num
    return result
