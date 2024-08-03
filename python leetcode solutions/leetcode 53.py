# leetcode 53
# Maximum Subarray

# brute force approach to calculate 
# all of the sums and sub arrays is O(N^3)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        l = 0 
        res = cur = nums[0]
        for r in range(1,len(nums)): 
            cur += nums[r]
            if cur < nums[r]: 
                l = r 
                cur = nums[r]

            res = max(res,cur)
        return res
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution().maxSubArray(nums)
print(test)

# Time Complexity: O(N)
# Space Complexity: O(1) 

'''

Brief Explanation: 

2 pointers/greedy approach
 
1. iterate the right pointer and increase the current sum.
2. iterate the left pointer only when current is \
        less than the value the right pointer. 
3. check the max sum. 

Similar Problem: leetcode 121

'''