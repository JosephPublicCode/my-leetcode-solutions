class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l+=1
        return nums
    
nums = [1,0,3,4,0,12]
test = Solution().moveZeroes(nums)
print(test)
    
# Time Complexeity: O(n)
# Space Complexeity: O(1)


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        for i in range(len(nums)):
            j = i
            while j < len(nums) and nums[j] == 0 : 
                j += 1

            if nums[i] == 0 and  j < len(nums): 
                nums[i], nums[j] =  nums[j], nums[i]

            
        return nums
    