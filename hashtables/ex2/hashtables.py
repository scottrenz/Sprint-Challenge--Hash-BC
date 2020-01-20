

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL handle collisions
# '''
n = 0
def hash_table_insert(hash_table, key, value):
    # index = hash(key, len(hash_table.storage))
    if key == "NONE":
        index = 1
    elif value == "NONE":
        index = hash_table.capacity-1
    else:        
        index = int(str(ord(key[0]))+str(ord(key[1]))+str(ord(key[2])))

    if value == "NONE":
        nextx = None
    else:        
        nextx = int(str(ord(value[0]))+str(ord(value[1]))+str(ord(value[2])))
    det_pair = None
    if nextx:
        if hash_table.storage[nextx] is None:
            det_pair = LinkedPair(value, None)
    new_pair = LinkedPair(key, value)
    if value != "NONE":
        if det_pair:
            new_pair.next = det_pair
        else:    
            new_pair.next = hash_table.storage[nextx]
    hash_table.storage[index] = new_pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is None:
        print("ERROR: Unable to remove entry with key " + key)
    else:
        if last_pair is None:  # Removing the first element in the LL
            hash_table.storage[index] = current_pair.next
        else:
            last_pair.next = current_pair.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]

    while current_pair is not None:
        if(current_pair.key == key):
            return current_pair.value
        current_pair = current_pair.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(2 * len(hash_table.storage))

    current_pair = None

    for i in range(len(hash_table.storage)):
        current_pair = hash_table.storage[i]
        while current_pair is not None:
            hash_table_insert(new_hash_table,
                              current_pair.key,
                              current_pair.value)
            current_pair = current_pair.next

    return new_hash_table
