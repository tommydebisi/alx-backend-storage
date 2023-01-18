#!/usr/bin/env python3
"""
    exercise mod
"""
import redis
from typing import Union
import uuid


class Cache:
    """
        Class that caches input to redis server
    """
    def __init__(self) -> None:
        """ constructor function """
        self.__redis = redis.Redis(host='localhost', port=6379)
        self.__redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """
            takes a data storing it with a unique id and returning
            the key
        """
        if data:
            key = uuid.uuid4()
            self.__redis.set(str(key), data)
            return str(key)
