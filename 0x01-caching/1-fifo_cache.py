#!/usr/bin/python3
""" Module for class FIFOCache"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """

    def __init__(self):
        """
        constructor for FIFOCache that calls parent's constuctor
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache, but
        if the no:of items in the dictionary is greater
        than BaseCaching.MAX_ITEMS the 1st item should
        be discarded as for the fifo algorithm
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # next(iter(dic)) removes 1st item
            # dict keeps insertion order
            key = next(iter(self.cache_data))
            del self.cache_data[key]
            print("DISCARD: {}".format(key))

        def get(self, key):
            """
            Get an item by key
            """
            if key is None:
                None

            elif key not in self.cache_data:
                None

            else:
                return self.cache_data.get(key)
