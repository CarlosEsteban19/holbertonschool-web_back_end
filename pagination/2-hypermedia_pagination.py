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
        info = {}
        rows: int = 0

        data = Server.dataset(self)
        for row in data:
            rows += 1

        totalPages = rows // page_size

        prevPage = page - 1
        if prevPage == 0:
            prevPage = None

        nextPage = page + 1
        if nextPage > totalPages:
            nextPage = None

        currentPage = Server.get_page(self, page, page_size)
        if not currentPage:
            page_size = 0

        info['page_size'] = page_size
        info['page'] = page
        info['data'] = currentPage
        info['next_page'] = nextPage
        info['prev_page'] = prevPage
        info['total_pages'] = totalPages
        return info


server = Server()
print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
