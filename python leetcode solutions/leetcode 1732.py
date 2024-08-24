# leetcode 1732 

# Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        pre_sum = [0 for i in range(n+1)]

        for i in range(1,n+1): 
            pre_sum[i] = pre_sum[i-1] + gain[i-1]
        return max(pre_sum)

# Time and Space O(n)

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        max_sum = 0
        tmp = 0 

        for g in gain: 
            tmp += g
            max_sum = max(tmp,max_sum)

        return max_sum
# Time O(n)
# Space O(1)
