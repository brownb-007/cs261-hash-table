# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Brayden Brown


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(size)]

    def __setitem__(self, key, value):
        index = self.hash(key)
        for key_and_value in self.data[index]:
            if key_and_value[0] == key:
                key_and_value[1] = value
        self.data[index].append([key, value])

    def __getitem__(self, key):
        index = self.hash(key)
        for key_and_value in self.data[index]:
            if key_and_value[0] == key:
                return key_and_value[1]

    def hash(self, key):
        return hash(key) % self.size

    
    pass
