# leetcode 238

# Product of Array Except Self

# most optimal method uses the prefix and suffix sum approach
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        suffix = []
        pre, suf = 1,1
        prefix.append(1)
        suffix.append(1)
        for i in range(len(nums)-1):
            pre *=nums[i]
            prefix.append(pre)
            suf *= nums[len(nums)-i-1]
            suffix.append(suf)
        i, j = 0, len(suffix)-1
        while i < len(prefix) and j >= 0:
            nums[i] = prefix[i]*suffix[j] 
            j -= 1
            i += 1
        return nums

nums = [2,5,7,9]
test = Solution().productExceptSelf(nums)
print(test)

# Time Complexeity: O(n)
# Space Complexeity (additional):O(1)

'''
Method: 

1. uses prefix and suffic sum methods. 
2. product of prefix and suffix sum gives the result. 
'''


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1 for i in range(len(nums))]
        i, j = 0, len(nums) - 1
        pre,suf = 1,1
        while i < len(nums) and j >=0:
            res[i] *= pre 
            res[j] *= suf
            pre *= nums[i]
            suf *= nums[j]
            j -= 1
            i += 1
        return res
nums = [2,5,7,9]
test = Solution().productExceptSelf(nums)
print(test)



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1 
        for i in range(len(nums)-1,-1,-1): 
            res[i] *= suffix
            suffix *= nums[i]
        return res
nums = [2,5,7,9]
test = Solution().productExceptSelf(nums)
print(test)
  
# too slow
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        map = {}
        for index, num in enumerate(nums):
            map[index] = num
        temp = 1 
        for identifier in map:
            temp = 1 
            for key in map: 
                if key == identifier: 
                    pass
                else: 
                    temp *= map[key]
            res.append(temp)
        return res
# this solution works however it is too slow

nums = [1,2,3,7,5]
test = Solution().productExceptSelf(nums)
print(test)

# uses list slicing and a product helper function. 
# also too slow
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[:i]+nums[i+1:]
            res.append(self.product(temp))
        return res


    def product(self, nums:list[int]) -> list[int]:
        res = 1
        for num in nums: 
            res *= num
        return res
nums = [1,2,3,7,5]
test = Solution().productExceptSelf(nums)
print(test)