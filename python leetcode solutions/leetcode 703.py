# leetcode 703

# Kth Largest Element in a Stream
import heapq


class KthLargest():

    def __init__(self, k:int, nums: list[int]):
        # The creation of the heap is O(N) time 
        self.k = k 
        heapq.heapify(nums)
        while len(nums) > k: 
            heapq.heappop(nums)
        self.nums = nums

    def add(self,val:int) -> int: 
        if len(self.nums) < self.k: 
            heapq.heappush(self.nums,val)
        else: 
            heapq.heappushpop(self.nums,val)
        return self.nums[0]


k = 3 
nums = [4,5,8,2]

test = KthLargest(k,nums)
print(test.add(3))
print(test.add(5))
print(test.add(10))
print(test.add(9))
print(test.add(4))

 
# O(n) time for creating the heap - popping could be as bad as O((n-1)logn)
# O(log n) for heappush and heappushpop

'''
Method: 
implementing a min heap data structure. 
1. use heapify if the heap 
2. if too large then continue to pop until the heap is the correct size. 
3. adding to the heap, if too large a pushpop must be used, else just push
4. access the first element in the heap as the k largest. 
'''
