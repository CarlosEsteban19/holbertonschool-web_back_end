#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """list all docs"""
    docs = list(mongo_collection.find())
    return docs
