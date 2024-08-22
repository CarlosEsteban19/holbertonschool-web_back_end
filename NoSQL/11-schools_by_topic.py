#!/usr/bin/env python3
"""task 11"""


def schools_by_topic(mongo_collection, topic):
    """school topic"""
    results = list(mongo_collection.find({'topics': topic}))
    return results
