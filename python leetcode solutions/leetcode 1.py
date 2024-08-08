# leetcode 1 
# the two sum problem

# The brute force method for this problem would be: 
# try every permutation until a result is returned that matches the target. 
#  this would be O(n^2) time. 
# as seen below
class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]: 
        indexmap = {}

        for i in range(len(nums)): 
            indexmap[i] = nums[i]
        
        j = 0 
        while j < len(nums): 
            for i in range(j+1,len(nums)): 
                if indexmap[j] + indexmap[i] == target:
                    return [j,i]
            j +=1
        return -1
nums = [2,7,11,15]
target = 13
test = Solution().twoSum(nums,target)
print(test) 



'''
Method: 
1. enumerate over nums
2. calculate diff
3. if diff in list return the value corresponding with diff and current index. 

'''
# Time Complexeity: O(n)
# Space Complexeity: O(n)

# alternative method
class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]: 
        indexmap = {}

        for i,num in enumerate(nums): 
            diff = target - num
            if diff in indexmap: 
                return [i,indexmap[diff]]
            indexmap[num] = i

nums = [2,7,11,15]
target = 13
test = Solution().twoSum(nums,target)
print(test) 

