# leetcode 643 

# Maximum Average Subarray I 

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)

        l, r = 0, k-1 
        sum = 0 
        for i in range(k): 
            sum += nums[i]

        max_sum = sum
        cur_sum = sum

        while r < n-1: 
            cur_sum -= nums[l]
            l += 1 
            r += 1 
            cur_sum += nums[r]


            max_sum = max(max_sum, cur_sum)
        return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4 
test = Solution().findMaxAverage(nums,k)
print(test)

'''
Method: 
Two pointer
1. initialize the sum and pointers
2. run the whole loop to obtain the maximum sum. 
'''


# list comprehension & for loop version
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        best = cur = sum(nums[:k])
        for i in range(k,len(nums)):
            cur += nums[i] - nums[i-k]
            if cur>best:
                best = cur
        return best/k