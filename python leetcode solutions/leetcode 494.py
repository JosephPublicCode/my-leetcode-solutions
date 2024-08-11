# leetcode 494 

# find the target sum ways. 

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cache = {}
        def dp(i,sum): 
            if i == len(nums): 
                if sum == target: 
                    return 1
                return 0
            if (i,sum) in cache: 
                return cache[(i,sum)]
            pos = dp(i+1,sum+nums[i])
            neg = dp(i+1,sum-nums[i])
            cache[(i,sum)] =  pos + neg
            return cache[(i,sum)]
        return dp(0,0)
        

nums = [1,1,1,1,1]
target = 3
test = Solution().findTargetSumWays(nums, target)
print(test)

#  Time Complexeity: O(n)
# Space Complexeity: 

'''
Method: 
Recursive Dynamic Programming approach using caching/memoization
1. pass (index, sum) into the cache
2. define innter helper recursive function. 
3. if index == len(nums): return 1 or 0 depending on if the total is equal to the target
4. if in cache return cache result
5. cache assignment: pos + neg, the binary choice between positive or negative at index i.
6. return the result of dp on the entire array
 
'''
