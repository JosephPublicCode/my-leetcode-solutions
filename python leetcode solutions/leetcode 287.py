class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # using floyd hare and tortoise algorithm. 
        slow, fast = 0,0
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break

        slow2 = 0 
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                break
        return slow
       

# nums = [1,3,4,3,2]

# test = Solution().findDuplicate(nums)
# print(test)
