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
    print("\tmethod GET: {}".format(collection.count_documents(
                                    {"method": "GET"})))
    print("\tmethod POST: {}".format(collection.count_documents(
                                    {"method": "POST"})))
    print("\tmethod PUT: {}".format(collection.count_documents(
                                    {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(collection.count_documents(
                                    {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(collection.count_documents(
                                    {"method": "DELETE"})))
    print("{} status check".format(collection.count_documents(
                                    {"path": "/status"})))
    print('IPs:')

    aggr_list = [
        {"$group": {
            "_id": "$ip", "ip_count": {"$sum": 1}
        }}, {"$sort": {"ip_count": -1}}, {"$limit": 10}
    ]
    for item in collection.aggregate(aggr_list):
        print("\t{}: {}".format(item.get("_id"),
                               item.get("ip_count")))
