# leetcode 198 

# House Robber

# dynamic programming method.
class Solution:
    def rob(self, nums:list[int]) -> int: 
        dp = [0]*(len(nums)+ 2)
        for i in range(len(nums)-1,-1,-1):
            p1 = dp[i+1]
            p2 = dp[i+2]
            dp[i] = max(nums[i] + dp[i+2], 
                        dp[i+1])
        return dp[0]
    
nums = [21,9,3,21]
test = Solution().rob(nums)
print(test)

# O(N) time complexeity
# O(N) space complexeity

'''

Method:
Bottom Up Dynamic programming

1. use array to store values with 2 spaces of padding.
2. to get current max compare previous to next previous + current and take the max value.

'''



# recursive could be improved with a memo/cache.
class Solution:
    def rob(self, nums:list[int]) -> int: 
        
        if len(nums) == 0: 
            return 0

        res =  max(self.rob(nums[2:])+nums[0],self.rob(nums[1:]))
        return res
        
# O(2^N) time complexeity (O(N) with a cache/memo).
# O(2^N ) space complexeity as well.
    
# O(1) space and O(N) time.
class Solution:
    def rob(self,nums:list[int]) -> int: 
        one, two = 0, 0
        for n in nums:
            temp = two
            two = max(n + one, two)
            one = temp
        return two
        
