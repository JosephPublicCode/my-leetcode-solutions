# leetcode 1049 

# Last Stone Weight

import math
class Solution(): 
    def lastStoneWeightII(self, stones:list[int]) -> int: 
        stoneSum = sum(stones)

        target = math.ceil(stoneSum / 2)

        def dfs(index, current):
            if current >= target or index == len(stones):
                return abs(current - (stoneSum - current)) 
            if (index,current) in dp: 
                return dp[(index,current)]
            dp[(index, current)] = min(dfs(index+1,current), dfs(index+1, current + stones[index]))

            return dp[(index, current)]
        
        dp = {}

        return dfs(0,0)
    
stones = [2,7,4,1,8,1]
test = Solution().lastStoneWeightII(stones)
print(test)

# Time Complexeity: O(n * total)
# Space complexeity: O( n * total)
'''
Method: 
dfs dynamic programming approach, bounded knapsack style function. 
1. find the target by splitting the sum in two using ceil to round up. 
2. base case, greater than or equal to the target we return the other pile. 
3. if in hashmap we return the cache value 
4. run dfs twice, include the value at i or do not include the value at i. 

'''



class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:

        n = len(stones)
        bigSum = sum(stones)

        pos = set([0])

        for index, stone in enumerate(stones):
            pos.update([stone+x for x in pos])
            print(pos)
        return min([abs(bigSum-2*i) for i in pos])

    
stones = [31,26,33,21,40]
test = Solution().lastStoneWeightII(stones)
print(test)
'''
Method: 
This process generates all the possible piles in the set of stones from any number of stones. 
The solution is then the minimization of total sum - 2* pile of stones that can be generated. 
'''