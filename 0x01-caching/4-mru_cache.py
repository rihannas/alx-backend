#!/usr/bin/python3
""" 3-main LRU Cache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ LRUCache inherit from BaseCaching """
    list_aux = []
    dict_aux = {}

    def __init__(self):
        """ Init instance BaseCaching """
        super().__init__()

    def put(self, key, item):
        """ Add LRU to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            """ find key by value """
            for k, v in self.dict_aux.items():
                if v == 1:
                    to_remove = k
                    del self.cache_data[to_remove]
                    break

            self.dict_aux = self.cache_data.copy()
            self.list_aux = list(self.dict_aux.keys())
            for i in self.list_aux:
                self.dict_aux[i] = 0
            self.dict_aux[key] += 1
            print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """ Get LRU to cache """
        if key is None or key not in self.cache_data:
            return None
        self.dict_aux = self.cache_data.copy()
        self.list_aux = list(self.dict_aux.keys())
        for i in self.list_aux:
            self.dict_aux[i] = 0
        self.dict_aux[key] += 1
        return self.cache_data[key]
