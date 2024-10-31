#!/usr/bin/env python3
"""
lfu cache
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    lfu cache implementation
    """
    def __init__(self):
        """
        Initialize cache data
        """
        super().__init__()
        self.count = {}

    def put(self, key: str, item: str) -> None:
        """
        Put item into cache
        """
        if key is not None and item is not None:
            if key in self.count.keys():
                self.cache_data[key] = item
                self.count[key] += 1
            elif (len(self.count) < BaseCaching.MAX_ITEMS):
                self.count[key] = 1
                self.cache_data[key] = item
            else:
                min_key = min(self.count, key=self.count.get)
                print(f"DISCARD: {min_key}")
                self.cache_data.pop(min_key)
                self.count.pop(min_key)
                self.cache_data[key] = item
                self.count[key] = 1

    def get(self, key: str) -> str:
        """
        Get item from cache
        """
        if key is not None and key in self.cache_data:
            self.count[key] += 1
            return self.cache_data[key]
        else:
            return None
