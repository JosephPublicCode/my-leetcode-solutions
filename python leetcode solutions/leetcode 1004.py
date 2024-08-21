class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        win = 0 
        max_win = 0 
        zeros = 0 
        l = 0 

        for r in range(n): 

            if nums[r] == 0: 
                zeros +=1

            while zeros > k:
                if nums[l] == 0: 
                    zeros -= 1 
                l += 1 
            win = r - l + 1 

            max_win = max(win,max_win)
        return max_win

nums =[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

k = 3

test = Solution().longestOnes(nums,k)
print(test)