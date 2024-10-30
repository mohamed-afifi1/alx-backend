#!/usr/bin/env python3
"""
fifo cache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    fifo cache implementation
    """
    def __init__(self):
        """
        Initialize cache data
        """
        super().__init__()
        self.queue = []

    def put(self, key: str, item: str) -> None:
        """
        Put item into cache
        """
        if key is not None and item is not None:
            if (len(self.queue) < BaseCaching.MAX_ITEMS) or key in self.queue:
                self.queue.append(key)
                self.cache_data[key] = item
            else:
                print(f"DISCARD: {self.queue[0]}")
                self.cache_data.pop(self.queue[0])
                self.queue.pop(0)
                self.queue.append(key)
                self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Get item from cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
