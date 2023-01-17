#!/usr/bin/env python3
"""
    11-schools_by_topic mod
"""


def schools_by_topic(mongo_collection, topic):
    """
        returns the list of school having a specific topic

        Args:
            topic: topic searched
            mongo_collection:
    """
    return mongo_collection.find({'topics': {'$in': [topic]}})
