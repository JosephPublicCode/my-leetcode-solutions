# leetcode 167

# Two Sum II - Input Array is Sorted. 

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1 

        while l < r: 
            twoSum = numbers[l] + numbers[r]
            if twoSum < target: 
                l += 1
            elif twoSum > target: 
                r -= 1
            else:
                return [l+1,r+1]
numbers = [2,7,11,15]
target = 9    
test = Solution().twoSum(numbers,target)
print(test)     

# Time Complexeity: O(n)
# Space Complexeity: O(1) 

'''

 1. initialise a right and left pointer
 2. check the sum
 3. if too small then increment the left pointer
 4. if too large then decrement the right pointer
 5. repeat the process until solution
 6. return [l + 1, r + 1] (as the list is indexed - 1)
'''