#!/usr/bin/env python3
"""
    101-students mod
"""


def top_students(mongo_collection):
    """
        returns all students sorted by average score

        Args:
            mongo_colection: pymongo collection object
    """
    aggr_list = [
        {"$project": {"_id": 1, "name": 1,
                      "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}},
    ]

    return mongo_collection.aggregate(aggr_list)
