# Leetcode 42 

# Trapping Rain Water

class Solution: 
    def trap(self, height: list[int]) -> int:
        if not height: 
            return 0
        l,r = 0, len(height) - 1 
        l_hei, r_hei = height[l], height[r]
        sum = 0 
        while l < r:
            diff = min(l_hei,r_hei)
            if l_hei <= r_hei: 
                sum += ((diff-height[l]) if (diff-l_hei) >= 0 else 0)
                l+=1
                l_hei = max(l_hei,height[l])
            else: 
                sum += ((diff-height[r]) if (diff-r_hei) >= 0 else 0)
                r-=1
                r_hei = max(r_hei,height[r])
        return sum
# Time Complexeity: O(n)
# Space complexeity: O(1)

'''
Method: 
Two pointer approach. 

Concept: 
The concept of this problem is that the amount of water that can be stored at a given position 
is determined by the maximum and minimum height either side of that point and then subtracting the height at that position. 
The reason for this is that if the height at the given poition is equal to or greater than the max and min either side the 
water will simply spill off the top and not be stored. 

eqn: stored = min(r_max,l_max) - current_height

Method: 
1. initialize a right and left pointer either side of the array. 
2. increment the pointer that is smaller, this is because we do not need the absolute max of r and l to get the correct result 
as long as we have the accurate bottleneck height value. 
3. compute the value being added to the sum
4. iterate the pointer adn recalculate the max. 

'''

# This solution is slightly more elegant, it is possible because my updating the relevant max first, in the worst case the max is 
# the current value so we add a 0. In all other cases the value will be +ve so no negative has to be dealt with
# Time Complexeity: O(n)
# Space complexeity: O(1)
class Solution: 
    def trap(self, height: list[int]) -> int:
        if not height: 
            return 0
        l,r = 0, len(height) - 1 
        l_hei, r_hei = height[l], height[r]
        sum = 0 
        while l < r:
            diff = min(l_hei,r_hei)
            if l_hei <= r_hei: 
                l+=1
                l_hei = max(l_hei,height[l])
                sum += (l_hei-height[l])
            else: 
                r-=1
                r_hei = max(r_hei,height[r])
                sum += (r_hei-height[r])
        return sum


# alternative, conceptually easy to understand but uses more memory. 

# Time Complexeity: O(n)
# Space complexeity: O(n)
class Solution: 
    def trap(self, height: list[int]) -> int:
        if not height: 
            return 0 
        cur_max = 0
        l_max = []
        for i in range(len(height)): 
            cur_max = max(cur_max,height[i])
            l_max.append(cur_max)
        cur_max = 0
        r_max = []

        for i in range(len(height)-1,-1,-1): 
            cur_max = max(cur_max,height[i])
            r_max.append(cur_max)

        r_max.reverse()
        sum = 0 
        for i in range(len(height)): 
            diff = min(l_max[i],r_max[i]) - height[i]
            if diff > 0: 
                sum += diff
        return sum

