#!/usr/bin/env python3
"""
    12-log_stats mod
"""
import pymongo


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(len(list(collection.find({
        "method": {'$in': ["GET"]}
        })))))
    print("\tmethod POST: {}".format(len(list(collection.find({
        "method": {'$in': ["POST"]}
        })))))
    print("\tmethod PUT: {}".format(len(list(collection.find({
        "method": {'$in': ["PUT"]}
        })))))
    print("\tmethod PATCH: {}".format(len(list(collection.find({
        "method": {'$in': ["PATCH"]}
        })))))
    print("\tmethod DELETE: {}".format(len(list(collection.find({
        "method": {'$in': ["DELETE"]}
        })))))
    print("{} status check".format(len(list(collection.find({
        "path": {'$in': ["/status"]}
        })))))
