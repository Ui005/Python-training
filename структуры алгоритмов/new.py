class HashMap(object):
    def __init__(self):
        self.hashmap = [[] for i in set(s)]

    def insert(self, key, value: int):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            n = (bucket[i][1] + 1)
            bucket[i] = ((key, n))
        else:
            bucket.append((key,value))

    def retrieve(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError


s = [i for i in input("введите строку: ") if i != " "]
hash_ = HashMap()
for i in s:
    hash_.insert(i,1)
print(hash_.hashmap)
print(hash("g"))
print(hash("h"))

