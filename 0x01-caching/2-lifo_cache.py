#!/usr/bin/env python3
"""
lifo cache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    fifo cache implementation
    """
    def __init__(self):
        """
        Initialize cache data
        """
        super().__init__()
        self.stack = []

    def put(self, key: str, item: str) -> None:
        """
        Put item into cache
        """
        if key is not None and item is not None:
            if key in self.stack:
                self.cache_data[key] = item
                self.stack.remove(key)
                self.stack.append(key)
            elif (len(self.stack) < BaseCaching.MAX_ITEMS):
                self.stack.append(key)
                self.cache_data[key] = item
            else:
                print(f"DISCARD: {self.stack[BaseCaching.MAX_ITEMS - 1]}")
                self.cache_data.pop(self.stack[BaseCaching.MAX_ITEMS - 1])
                self.stack.pop(BaseCaching.MAX_ITEMS - 1)
                self.stack.append(key)
                self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Get item from cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
