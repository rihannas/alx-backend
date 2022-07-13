#!/usr/bin/python3
""" Module for class BasicCache """

from base_caching import BaseCaching


"""
You must use self.cache_data -dict from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dict self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            pass

        else:
            self.cache_data[key] = item

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
