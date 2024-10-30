#!/usr/bin/env python3
"""
basic cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key: str, item: str) -> None:
        """
        Put item into cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Get item from cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
