# leetcode 875

# KoKo Eating Bananas


class Solution:

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # this is the maximum speed that can be min. 

        left, right = 1,max(piles)
        res = right
        while left <= right: 
            mid = (left + right)//2
            # print(mid)
            hoursTaken = 0 
            for pile in piles: 
                hoursTaken += (pile // mid \
                               if pile % mid == 0\
                                  else (pile // mid) + 1)
            if hoursTaken <= h: 
                # print(mid, res)
                res = min(mid, res) 
                right = mid -1 
            elif hoursTaken > h: 
                left = mid + 1  
        return res
    
test = Solution().minEatingSpeed([3,6,7,11],8)
print(test)

# Time Complexeity: O(n log max(piles))

# Space Complexeity: O(1)

'''
Method: 
Modified Binary Search
1. setup binary search
2. run for loop to see if all the bananas will be eaten in time
3. if yes then try mid - 1
4. if not then move the left pointer to mid + 1 as in a normal binary search

Time Complexeity: 
n component is to iterate in the for loop and log max(piles) is due to the binary search

'''