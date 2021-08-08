class HashTable:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(0, self.size)]
        #print(self.hashmap)

    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('dose not exist')

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


H = HashTable()

H['key1'] = 'value1'

print(H['key1'])


H.set(10,'value1')
H.set(20,'value2')
H.set('key3','value3')

print(H.get(10))
print(H.hashmap)