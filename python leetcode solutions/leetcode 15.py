# leetcode 15

# The Three Sum Problem


class Solution: 
    def threeSum(self,nums:list[int]) -> list[list[int]]: 
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if (i > 0 and a == nums[i-1]):
                continue
            l,r = i + 1, len(nums) -1 
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: 
                    r -=1
                elif threeSum < 0: 
                    l +=1
                else: 
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
        return res
    
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]   
test = Solution().threeSum(nums)
print(test)

# Time Complexeity: O(n^2)
# Space Complexeity: O(n)

'''
Method: 
sort the numbers: O( n log n) 
binary search style: O( n log n)
modified method of the two sum approach. 

1. enumerate through the list with index, i. 
 - continue statement check is used to insure we do not get duplicates. 
2. set the binary search pointers as i+1, len(nums) -1 
3. if three sum > 0, r -= 1 (decrease the sum).
4. if three sum < 0, l += 1 (increase the sum). 
5. if equal append this to the result then l += 1. 
6. to avoid duplicates, with nums[l] == nums[l - 1] we continue to iterate. 
- shifting to the right is not necessary as the algorithm will automatically do this without the while loop that is used for left. 
'''
