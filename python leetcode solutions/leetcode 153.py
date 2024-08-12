# leetcode 153

# Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0, len(nums) - 1 
        if nums[l] < nums[r] or len(nums) ==1: 
            return nums[l]
        while l <= r: 
            mid = r + (l-r)//2
            if mid != 0 and nums[mid-1] > nums[mid]: 
                return nums[mid]
            elif nums[mid] >= nums[0]: 
                l = mid + 1
            else: 
                r = mid - 1
# Time Complexeity: O(log n)
# Space Complexeity: O(1)

'''
Method: 
modified Binary Search
1. check if the list has not been rotated. 
2. modified BS, if mid -1 > mid we are at the pivot to return nums[mid]
3. if nums[mid] >= nums[0]: l = mid + 1 therefore part of the left sorted portion so search to the right
4. else in the right sorted so find the pivot point. 
'''

# my original solution. 
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        l,r = 0, len(nums) - 1 
        while l <= r: 
          
            mid = r + (l-r)//2
            if (nums[l] <= nums[mid] and nums[r] > nums[mid]):
                return nums[l]
            if (nums[l] >= nums[mid] and nums[r] < nums[mid]):
                return nums[r]
            elif nums[mid-1] > nums[mid]: 
                return nums[mid]
            elif nums[l] < nums[mid] and nums[r] < nums[mid]: 
                l = mid + 1 
            elif nums[l]> nums[mid] and nums[r] > nums[mid]: 
                r = mid - 1 
