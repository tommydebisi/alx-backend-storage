#!/usr/bin/env python3
"""
    exercise mod
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


ReturnData = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """ decorator function for cache class that counts calls """
    @wraps(method)
    def inner(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args, **kwargs)
    return inner


def call_history(method: Callable) -> Callable:
    """
        tore the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def inner(self, *args):
        key_in = "{}:inputs".format(method.__qualname__)
        key_out = "{}:outputs".format(method.__qualname__)

        id_str = method(self, *args)

        # storing the input and output args
        self._redis.rpush(key_in, str(args))
        self._redis.rpush(key_out, id_str)
        return id_str
    return inner


def replay(method):
    """
        display the history of calls of a particular function.
    """
    db_instance = redis.Redis()
    meth_name = method.__qualname__

    # get val associated wwith meth_name
    bs = db_instance.get(meth_name)

    if not bs:
        return

    print("{} was called {} times:".format(meth_name, bs.decode("utf-8")))

    input_list = db_instance.lrange(f"{meth_name}:inputs", 0, -1)
    output_list = db_instance.lrange(f"{meth_name}:outputs", 0, -1)

    for inp, out in zip(input_list, output_list):
        print(f"{meth_name}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    """
        Class that caches input to redis server
    """
    def __init__(self) -> None:
        """ constructor function """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: ReturnData) -> str:
        """
            takes a data storing it with a unique id and returning
            the key
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> ReturnData:
        """
            returns the value goten from the key in database
        """
        val = self._redis.get(key)
        return fn(val) if fn else val

    def get_str(self, key: str) -> str:
        """ returns a string value from database """
        return self.get(key, lambda d: d.encode("utf-8"))

    def get_int(self, key: str) -> int:
        """ returns a int value from database """
        return self.get(key, int)
