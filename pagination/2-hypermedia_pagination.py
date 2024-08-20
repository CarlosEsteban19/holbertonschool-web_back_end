#!/usr/bin/env python3
"""0-simple_helper_function.py"""
from typing import Tuple, List, Dict
import csv


def index_range(page: int, page_size: int) -> Tuple:
    """0-simple_helper_function.py"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """1-simple_pagination.py"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = Server.dataset(self)
        limit = index_range(page, page_size)

        return data[limit[0]:limit[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """2-hypermedia_pagination.py"""
        data = Server.dataset(self)
        rows = len(data)

        totalPages = (rows + page_size - 1) // page_size

        prevPage = page - 1 if page > 1 else None
        nextPage = page + 1 if page < totalPages else None

        currentPage = Server.get_page(self, page, page_size)
        actualSize = len(currentPage)

        return {
            'page_size': actualSize,
            'page': page,
            'data': currentPage,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages,
        }
