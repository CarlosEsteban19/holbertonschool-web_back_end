#!/usr/bin/env python3
"""task 10"""


def update_topics(mongo_collection, name, topics):
    """update topics"""
    mongo_collection.update_many({'name': name}, {"$set": {'topics': topics}})
