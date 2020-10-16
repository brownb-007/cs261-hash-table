# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Brayden Brown


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(size)]

    def __setitem__(self, key, value):
        placeholder = self.hash(key)
        for key_and_value in self.data[placeholder]:
            if key_and_value[0] == key:
                key_and_value[1] = value
                return
        self.data[placeholder].append([key, value])

    def __getitem__(self, key):
        placeholder = self.hash(key)
        for key_and_value in self.data[placeholder]:
            if key_and_value[0] == key:
                return key_and_value[1]

    def hash(self, key):
        return hash(key) % self.size

    def delete(self, key):
        placeholder = self.hash(key)
        for key_and_value in self.data[placeholder]:
            if key_and_value[0] == key:
                self.data[placeholder].remove(key_and_value)

    def clear(self):
        self.data.clear()
        self.data = [[] for i in range(self.size)]

    def keys(self): 
        keys = [] 
        for i in range(self.size):
            for key in self.data[i]:
                keys.append(key[0])
        return keys

    def values(self): 
        values = [] 
        for i in range(self.size):
            for value in self.data[i]:
                values.append(value[1])
        return values

    pass
