#!/usr/bin/env python3
"""task 8"""
from typing import List
from pymongo import MongoClient


def list_all(mongo_collection) -> List:
    """list all docs"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['my_db']
    collection = db[mongo_collection]
    documents = collection.find()

    return [doc for doc in documents]
