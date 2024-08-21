#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """3-hypermedia_del_pagination.py"""
        data = Server.indexed_dataset(self)
        assert index < len(data)
        next_index = index + page_size

        currentPage = []
        tempIndex = index
        for _ in range(page_size):
            try:
                currentPage.append(data[tempIndex])
                tempIndex += 1
            except KeyError:
                tempIndex += 1
                currentPage.append(data[tempIndex])
                tempIndex += 1
                next_index += 1

        return {
            'index': index,
            'data': currentPage,
            'page_size': page_size,
            'next_index': next_index
        }
