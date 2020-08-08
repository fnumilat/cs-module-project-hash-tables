class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # create a var name for the instance of capacity
        self.capacity = capacity

        # if capacity is smaller than the min capacity
        # then point the capacity to the mind capacity
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        # create a storage that stores the result of 
        # the storage times the capacity
        self.storage = [None] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return the capacity
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_index = 5381
        hash_bytes = key.encode()

        for byte in hash_bytes:
            hash_index = ((hash_index << 5) + hash_index) + byte
        return hash_index


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # Day 1:
        # hash the key
        # create a var for hash_index
        # hash_index = self.hash_index(key)
        # # call the storage and pass the hash_index to it
        # # and point it to the Linked List HashTableEntry passing the key and value
        # self.storage[hash_index] = HashTableEntry(key, value)

        # Day 2:
        # hash the key
        # create a var for hash_index
        hash_index = self.hash_index(key)
        # get the hash index in the the storage
        # and create a var for it called node
        node = self.storage[hash_index]

        # see if the node is set to none
        # set the hash index in the storage to the Linked List 
        # hash table entry and get the key and value
        # then increase the size by one
        if node is None:
            self.storage[hash_index] = HashTableEntry(key, value)
            self.size += 1
            # if the get load factore is bigger than 0.7
            # resize the capacity two times bigger
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
            return

        # set the prev to none
        prev = None

        # see if node is not none
        # then set the prev to node
        # and point the node to the next node
        while node is not None:
            prev = node
            node = node.next
            # and if the prev key is the current key
            # then set the prev value to the current value
            if prev.key == key:
                prev.value = value
                return
        # set the prev next to the Linked List hash table entry
        # and get the key and value
        # then increase the size by one
        prev.next = HashTableEntry(key, value)
        self.size += 1
        # if the get load factore is bigger than 0.7
        # resize the capacity two times bigger
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity *2)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # Day 1:
        # hash the key
        # # create a var for hash_index
        # hash_index = self.hash_index(key)
        # # see if the value in the storage is not set to none
        # # then set it to none
        # if self.storage[hash_index] is not None:
        #     self.storage[hash_index] = None
        # # and otherwise print
        # else:
        #     print("Key is not found!")

        
        # Day 2:
        # hash the key
        # create a var for hash_index
        hash_index = self.hash_index(key)
        # get the hash index in the the storage
        # and create a var for it called node
        node = self.storage[hash_index]

        # set the prev to none
        prev = None

        # see if the node is set at not none and of the 
        # node key is not equal to the key
        # then set the prev to node
        # and point the node to the next node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # and if node is set to none
        # the return the "Key is not found!"
        if node is None:
            return "Key is not found!"
        # otherwise if the prev is set to none
        # then set the hash index in the storage to the next node
        # and if not then set the prev and next to the next node
        else:
            if prev is None:
                self.storage[hash_index] = node.next
            else:
                prev.next = node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # hash the key
        # create a var for hash_index
        hash_index = self.hash_index(key)
        # see if the value in the storage is not set to none
        # if not then return the value of the key in the storage
        if self.storage[hash_index] is not None:
            return self.storage[hash_index].value
        # otherwise return none
        else:
            return None



    def resize(self,  value):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # create a new var called old capactiy
        # and set the storage to the old capacity var
        old_capacity = self.storage
        # set the capacity to the value
        self.capacity = value
        # create another var for the new capacity
        # and set the storage to the new capacity var
        new_capacity = [None] * self.capacity
        self.storage = new_capacity

        # set the size to 0
        self.size = 0

        # loop through the old capacity
        # set the current node to the index
        for i in old_capacity:
            cur_node = i
            # and see if the current node is set at not none
            # push the current node key and value to the storage
            # and set the current node to the next one
            while cur_node is not None:
                self.put(cur_node.key, cur_node.value)
                cur_node = cur_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
