#!/usr/bin/env python3
"""task 8"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """list all docs"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['my_db']
    collection = db[mongo_collection]
    documents = collection.find()
    docs = []
    for doc in documents:
        docs.append(doc)
    return docs
