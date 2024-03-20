from replacement_algorithm.LRU import LRU
from collections import deque

class Cache:
    def __init__(self, set, way):
        self._set = set
        self._way = way
        self._storage = [deque() for _ in range(set)]
    
    def get(self, key):
        set_index = self.hash_function(key)
        cache = LRU(self._storage, self._way)
        cache_value = cache.get(key, set_index)
        return cache_value
    
    def put(self, key, data):
        if key > (self._set * self._way) + self._way:
            return 

        set_index = self.hash_function(key)
        cache = LRU(self._storage, self._way)
        cache.add(set_index, key, data)
        return

    def hash_function(self, key):
        set_index = key // (self._way +1)
        return set_index
    
    def print_cache(self):
        for queue in self._storage:
            print(queue)
        return

if __name__ == '__main__':
    #create a n way associative cache with m set
    n, m = 4, 5
    n_way_associative_cache = Cache(n,m)
    n_way_associative_cache.print_cache()