#!/usr/bin/env python3
"""
    9-insert_school mod
"""


def insert_school(mongo_collection, **kwargs):
    """
        returns new _id after insertion into database
    """
    if not kwargs:
        return

    mongo_collection.insert_one(kwargs)
    return mongo_collection.find_one(kwargs).get('_id')
