from my_linked_list import *

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Yes, HashTableEntry({self.key}, {self.value})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` array
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.array = [None] * capacity

    def __repr__(self):
        return f'Yes, HashTable({self.array}, {self.capacity})'


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.array)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key): # This one, or ------------------------------------
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key): # This one --------------------------------------
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF



    def hash_index(self, key): # -------------------------------------------------
        """
        Take an arbitrary key and return a valid integer index
        between within the bucket capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        # print('hash index', self.djb2(key) % self.capacity)
        return self.djb2(key) % self.capacity

    def put(self, key, value): # ------------------------------------------
        """
        Hash collisions should be handled with Linked List Chaining.
        """
        # steps for a put ------------------------------------------
        ## hash the key to a value for the index
        ## Search linked list to see if the key already exists
        ##  if the key exists, replace the value
        ##  if not, create a new hash table entry
        index = self.hash_index(key)
        # self.array[index] = value
        # print('This is some value', value)

        # new_node = HashTableEntry

        # If there is None, create a linked list with a hash table entry at index of array if the index has nothing. 
        if self.array[index] == None:
            self.array[index] = LinkedList()
            self.array[index].add_to_tail(HashTableEntry(index, value))
        elif self.array[index]:
            self.array[index].add_to_tail(HashTableEntry(index, value))
            print('Does it exist', self.array[index].contains(key))
        


    def delete(self, key): # --------------------------------------------------
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.array[self.hash_index(key)] = None

        # if self.array[index] == True:


        # Lecture code
        # value = self.table[self.hash_index(key)]
        # if value == None:
        #     print('value is already None')
        # self.table[self.hash_index(key)] = None

    def get(self, key): # ---------------------------------------------------
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        return self.array[self.hash_index(key)]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


    def details(self):
        print('The details', self.array)
        # return self.array



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
    # ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

    x = HashTable(10)

    x.put('soo', 'wack!')
    x.put('ha', 'way wack!')
    x.put('unsure', 'the wackness is back')
    x.put('yet', 'another wacker')
    x.put('yet', 'another wacker ducky')
    
    # print(repr())
    x.get('soo')
