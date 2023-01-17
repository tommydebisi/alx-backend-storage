#!/usr/bin/env python3
"""
    10-update_topics mod
"""


def update_topics(mongo_collection, name, topics):
    """
        This function changes all topics of a school
        document based on the name given
    """
    mongo_collection.update_one({'name': name}, {
        '$set': {'topics': topics}
        }, upsert=True)
