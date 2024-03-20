from replacement_algorithm.IReplacementAlgo import IReplacementAlgo

class LRU(IReplacementAlgo): 
    def __init__(self, linked_list, capacity):
        self.storage = linked_list
        self.capacity = capacity

    def get(self, key, set_index):
        if key in self.storage[set_index][0]:
            return self.storage[set_index][0][key]

        for key_pair in self.storage[set_index]:
            if key in key_pair:
                self.storage[set_index].remove(key_pair)
                self.storage[set_index].appendleft(key_pair)
                return key_pair[key]

        return -1

    def add(self, set_index, key, value):
        if len(self.storage[set_index]) >= self.capacity:
            self.storage[set_index].pop()
            self.storage[set_index].appendleft({key:value})
        else:
            self.storage[set_index].append({key:value})
        
        return
