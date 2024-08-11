# leetcode 1046

# Last Stone Weight

import heapq

class Solution(): 
    def lastStoneWeight(self, stones:list[int]) -> int: 
        invertedStones = [-x for x in stones]
        heapq.heapify(invertedStones)
        while len(invertedStones) > 1: 
            first = heapq.heappop(invertedStones)
            second = heapq.heappop(invertedStones)
            if first != second:
                heapq.heappush(invertedStones,first - second)
        if len(invertedStones) == 1: 
            return abs(invertedStones[0])
        else: 
            return 0 

nums = [2,7,4,1,8,2]
test = Solution().lastStoneWeight(nums)
print(test)

#  Time Complexeity: O( n log n)
#  Space Complexeity: O(n)

''' 
Method: 
Implement using a max heap data structure. 
python does not support max heaps natively so inverting the list is used to get around this. 
1. invert the stones
2. heapify the stones
3. pop two stones
4. break the stones if not equal then append the difference as a new stone


''' 