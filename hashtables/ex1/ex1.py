#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(max(weights)+1)

    """
    YOUR CODE HERE
    """
    for i in range(0, length):
        hash_table_insert(ht,weights[i],i)

    for j in ht.storage:
        if j:
            try:
                if j.key != limit-j.key and ht.storage[limit-j.key] and j.value > ht.storage[limit-j.key].value:
                    return (j.value,ht.storage[limit-j.key].value)
            except:
                pass        
            if j.next:
                if j.next.key + j.key == limit:
                    if j.value > j.next.value:
                        return (j.value,j.next.value)
                    return (j.next.value,j.value)    
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")

