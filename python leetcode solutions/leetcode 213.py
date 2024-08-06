# leetcode 213

# House Robber II 

class Solution:
    def rob(self, nums: list[int]) -> int:
        housesFirst = [0 for _ in range(len(nums)+1)]
        housesLast = [0 for _ in range(len(nums)+1)]
        numsNoLast = nums[:-1]
        numsNoFirst = nums[1:]

        for i in range(len(nums)-2,-1,-1):
            housesFirst[i] = max(housesFirst[i+1],numsNoLast[i]+housesFirst[i+2])
            housesLast[i] = max(housesLast[i+1],numsNoFirst[i]+housesLast[i+2])

        return max(housesFirst[0],housesLast[0])
    
test = Solution().rob([17,4,5,3,4])
print(test)

# Time O(N) complexeity
# Space O(N) complexeity

'''
Method: 

It is always true that you cannot have the first element and the last element in the same max solution.
This means that you can run the standard house robber I style algorithm for the lists sliced at the beginning
and at the end. 

1. setup an array of zeros of length len(nums) + 1 this has 2 elements of padding. 
2. then do bottom up dynamic programming by comparing the previous to the next previous + current and take the max. 
3. return the max of this process on both sliced arrays. 

Similar Problem: leetcode 198

'''

# alternative uses a helper function instead of a combined loop. 

class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0],self.dp(nums[:-1]),self.dp(nums[1:]))
    def dp(self,array): 
        vector = [0 for _ in range(len(array)+2)]
        for i in range(len(array)-1,-1,-1):
            vector[i] = max(vector[i+1],array[i]+vector[i+2])
        return vector[0]
test = Solution().rob([17,4,5,3,4])
print(test)

'''
You can also do this with O(1) space and this is done by using pointers instead of a dp array. 
Time complexeity is the same for both methods. 
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0],self.dp(nums[:-1]),self.dp(nums[1:]))
    
    def dp(self,array): 
        one,two = 0,0
        for i in range(len(array)-1,-1,-1):
            temp = two 
            two = max(two,array[i]+one)
            one = temp
        return two
            
    
test = Solution().rob([17,4,5,3,4])
print(test)