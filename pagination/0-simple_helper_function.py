#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end index for pagination."""
    if page <= 0 or page_size <= 0:
        return (0, 0)
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
