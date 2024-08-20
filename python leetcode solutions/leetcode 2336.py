# leetcode 2336

# Smallest number in an Infinite Set

import heapq as hp 
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.cur = 1 

    def popSmallest(self) -> int:
        if self.heap: 
            return hp.heappop(self.heap)
        cur = self.cur 
        self.cur += 1 
        return cur
        

    def addBack(self, num: int) -> None:
        if num not in self.heap and num < self.cur: 
            hp.heappush(self.heap, num)

# Time Complexeity: O( log n ) for both
# Space Complexeity: O(n)

'''
Method: 
there are many possible ways to do this: 
- priority queue
- heap and set 
- set

All three have been done. Note: the second solution is only possible because of the leetcode constraint: 1 <= nums <= 1000. 
'''


import heapq as hp 
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1001)]
        self.set = set(self.heap)
        hp.heapify(self.heap)


    def popSmallest(self) -> int:
        val = hp.heappop(self.heap)
        self.set = set(self.heap)
        return val
        

    def addBack(self, num: int) -> None:
        if num not in self.set: 
            hp.heappush(self.heap,num)
            self.set.add(num)

import heapq as hp 
class SmallestInfiniteSet:

    def __init__(self):
        self.set = set()
        self.cur = 1 


    def popSmallest(self) -> int:
        if self.set: 
            res =  min(self.set)
            self.set.remove(res)
            return res
        res = self.cur 
        self.cur +=1 
        return res

    def addBack(self, num: int) -> None:
        if num < self.cur: 
            self.set.add(num)

# Time Complexeity: O(n), O(1)
# Space Complexeity: O(n)