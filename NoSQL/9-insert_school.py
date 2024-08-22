#!/usr/bin/env python3
"""task 9"""


def insert_school(mongo_collection, **kwargs):
    """insert doc into coll"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
