#!/usr/bin/env python3
"""
    8-all mod
"""


def list_all(mongo_collection):
    """
        returns pymongo collection object which can be iterated
        or an empty list
    """
    if not mongo_collection.count_documents({}):
        return []
    return mongo_collection.find()
