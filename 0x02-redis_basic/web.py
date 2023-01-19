#!/usr/bin/env python3
"""
    web mod
"""
import redis
import requests
from typing import Callable
from functools import wraps


def count_url(func: Callable) -> Callable:
    """ decorator function """
    @wraps(func)
    def inner(*args, **kwargs):
        red_instance = redis.Redis()

        if args:
            key = "count:{}".format(args[0])
        else:
            key = "count:{}".format(kwargs.get('url'))

        if not red_instance.exists([key]):
            red_instance.setex(key, 10, 1)
        else:
            red_instance.incr(key, 1)
        return func(*args, **kwargs)
    return inner


@count_url
def get_page(url: str) -> str:
    """
        uses the requests module to obtain the HTML content of a
        particular URL and returns it
    """
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    inst = redis.Redis()
    url = "https://intranet.alxswe.com/projects/1234#task-11668"
    print(get_page(url))
    # get_page(url)
    # count = inst.get("count{}".format(url))
    # print(count.decode("utf-8"))
