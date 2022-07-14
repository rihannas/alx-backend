#!/usr/bin/python3
""" 3-main LRU Cache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherit from BaseCaching """
    list_aux = []

    def __init__(self):
        """ Init instance BaseCaching """
        super().__init__()

    def put(self, key, item):
        """ Add LRU to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if self.list_aux.count(key) == 0:
            self.list_aux.append(key)
        else:
            for i in self.list_aux:
                if i == key:
                    self.list_aux.remove(i)
                    break
            self.list_aux.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.list_aux[0]]
            to_remove = self.list_aux[0]
            self.list_aux.remove(self.list_aux[0])
            print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """ Get LRU to cache """
        if key is None or key not in self.cache_data:
            return None
        if self.list_aux.count(key) == 0:
            self.list_aux.append(key)
        else:
            for i in self.list_aux:
                if i == key:
                    self.list_aux.remove(i)
                    break
            self.list_aux.append(key)
        return self.cache_data[key]
