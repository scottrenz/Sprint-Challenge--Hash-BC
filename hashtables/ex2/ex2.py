#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # hashtable = HashTable(length)
    maxi = 0
    a = []
    for i in tickets:
        if i.source != "NONE":
            if int(str(ord(i.source[0]))+str(ord(i.source[1]))+str(ord(i.source[2]))) > maxi:
                maxi = int(str(ord(i.source[0]))+str(ord(i.source[1]))+str(ord(i.source[2])))

    hashtable = HashTable(maxi+2)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        hash_table_insert(hashtable,i.source,i.destination)

    route = []
    nextv = hashtable.storage[1].next
    while nextv:
        nex = int(str(ord(nextv.key[0]))+str(ord(nextv.key[1]))+str(ord(nextv.key[2])))
        if hashtable.storage[nex] is None:
            break
        route.append(hashtable.storage[nex].key)    
        nextv = hashtable.storage[nex].next
    route.append(hashtable.storage[maxi + 1].key)    
    route.append(hashtable.storage[maxi + 1].value)    
    return route
