#!/usr/bin/env python3
"""mirame ahora hahahahaha"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """algo me dice q esto va"""
    return [(i, len(i)) for i in lst]
