# leetcode 11

# container with most water

# left and right pointer. 

# move the smallest pointer

# record the max area made between the two pointers. 



class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) -1 
        res = 0 

        while left < right: 
            lheight = height[left]
            rheight = height[right]
            minh = min(lheight,rheight)
            res = max(res,(right - left)*(minh))
            if lheight <= rheight: 
                left += 1 
            else: 
                right -= 1 
        return res
    
heights = [1,8,6,2,5,4,8,3,7]
test = Solution().maxArea(heights)
print(test)

# Time Complexeity: O(n)
# Space Complexeity: O(1)

'''
Method: 
2 pointer approach

1. initialize pointers at each end
2. calculate area as minH (of l and r pointers) * gap between r - l pointers. 
3. squeeze pointers together by incrementing/decrementing the one with the smallest height
4. record max result so far. 

'''