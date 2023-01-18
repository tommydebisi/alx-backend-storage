#!/usr/bin/env python3
"""
    exercise mod
"""
import redis
from typing import Union, Callable, Optional
import uuid


ReturnData = Union[str, bytes, int, float]
class Cache:
    """
        Class that caches input to redis server
    """
    def __init__(self) -> None:
        """ constructor function """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: ReturnData) -> str:
        """
            takes a data storing it with a unique id and returning
            the key
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]=None) -> ReturnData:
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
