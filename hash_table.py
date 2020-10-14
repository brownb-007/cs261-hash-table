# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Brayden Brown


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(size)]

    def __setitem__(self, key, value):
        index = self._hashed(key)
        for key_and_value in self.data[index]:
            if key_and_value[0] == key:
                key_and_value[1] = value
        self.data[index].append([key, value])

    def _hashed(self, key):
        return hash(key) % self.size

    pass
