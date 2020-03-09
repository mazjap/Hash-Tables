# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        return hash(key)


    # def _hash_djb2(self, key):
    #     pass


    def _hash_mod(self, key):
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        ll = LinkedPair(key, value)
        index = self._hash_mod(key)

        if self.storage[index] is None:
            self.storage[index] = ll
        else:
            node = self.storage[index]
            while node.next:
                if node.key is key:
                    node.value = value
                    return
                node = node.next
            
            node.next = ll
            

    def remove(self, key):
        self.storage[self._hash_mod(key)] = None


    def retrieve(self, key):
        node = self.storage[self._hash_mod(key)]
        while node:
            if node.key is key:
                return node.value
            node = node.next


    def resize(self):
        oldStorage = self.storage
        self.capacity = len(self.storage) * 2
        self.storage = [None] * self.capacity
        for i in range(len(oldStorage)):
            node = oldStorage[i]
            while node:
                self.insert(node.key, node.value)
                node = node.next



if __name__ == "__main__":
    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
    ht = HashTable(8)
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

    ht.insert("key-0", "new-val-0")
    ht.insert("key-1", "new-val-1")
    ht.insert("key-2", "new-val-2")
    ht.insert("key-3", "new-val-3")
    ht.insert("key-4", "new-val-4")
    ht.insert("key-5", "new-val-5")
    ht.insert("key-6", "new-val-6")
    ht.insert("key-7", "new-val-7")
    ht.insert("key-8", "new-val-8")
    ht.insert("key-9", "new-val-9")
    
    return_value = ht.retrieve("key-0")
    print(f'{return_value} == new-val-0: {return_value is "new-val-0"}')
    return_value = ht.retrieve("key-1")
    print(f'{return_value} == new-val-1: {return_value is "new-val-1"}')
    return_value = ht.retrieve("key-2")
    print(f'{return_value} == new-val-2: {return_value is "new-val-2"}')
    return_value = ht.retrieve("key-3")
    print(f'{return_value} == new-val-3: {return_value is "new-val-3"}')
    return_value = ht.retrieve("key-4")
    print(f'{return_value} == new-val-4: {return_value is "new-val-4"}')
    return_value = ht.retrieve("key-5")
    print(f'{return_value} == new-val-5: {return_value is "new-val-5"}')
    return_value = ht.retrieve("key-6")
    print(f'{return_value} == new-val-6: {return_value is "new-val-6"}')
    return_value = ht.retrieve("key-7")
    print(f'{return_value} == new-val-7: {return_value is "new-val-7"}')
    return_value = ht.retrieve("key-8")
    print(f'{return_value} == new-val-8: {return_value is "new-val-8"}')
    return_value = ht.retrieve("key-9")
    print(f'{return_value} == new-val-9: {return_value is "new-val-9"}')