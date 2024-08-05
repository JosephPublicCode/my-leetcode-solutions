# leetcode 146 

# LRU Cache


class ListNode(): 
    def __init__(self, key,val, next=None, prev=None):
        self.val, self.key = val, key
        self.next = next
        self.prev = prev 
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.cache = {}
        self.head, self.tail = ListNode(0,0), ListNode(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node): 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node): 
        prev = self.tail.prev
        prev.next, node.prev = node, prev
        self.tail.prev, node.next = node, self.tail

    def get(self, key: int) -> int:
        if key in self.cache: 
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        
        else: 
            return -1

    def put(self, key: int, value: int) -> None: 
        if key in self.cache: 
            self._remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity: 
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
            

LRUCacheTest = LRUCache(2)
print(LRUCacheTest.get(2))
print(LRUCacheTest.put(2,6))
print(LRUCacheTest.get(1))
print(LRUCacheTest.put(1,5))
print(LRUCacheTest.put(1,2))
print(LRUCacheTest.get(1))
print(LRUCacheTest.get(2))

'''

O(1) time complexeity, for the put and get operations. 
O(N) space complexeity.

method: 
1. use a hashmap pointing to doubly linked list nodes as the data structure. 
2. create insert and remove helper functions
    removing requires next and previous manipulations and deletion from the cache. 
    inserting requires next and previous manipulations at the end of the list and inserting into the cache. 
3. get uses the O(1) search of a dictionary/hashmap
4. put uses the tail of the doubly linked list to obtain O(1) time complexeity. 

Could use collections ordered dictionary to obtain a shorter solution. 

'''
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict: 
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict: 
            self.dict.move_to_end(key)
        else: 
            if len(self.dict)>=self.capacity: 
                self.dict.popitem(False)
        self.dict[key] = value
