# leetcode 309 

# Best Time to Buy and Sell a Stock with Cooldown. 

class Solution:


    def maxProfit(self, prices: list[int]) -> int:
        
        # key = (i,bool)
        memo = {} 

        def dfs(i,buying):
            if i >= len(prices):
                return 0 
            if (i,buying) in memo: 
                return memo[(i,buying)]
            if buying == True: 
                buy = dfs(i+1,False)-prices[i]
                cooldown = dfs(i+1,buying)
                memo[(i,buying)] = max(buy, cooldown)
                # if buying == False:
            else: 
                sell = dfs(i+2,True) + prices[i]
                cooldown = dfs(i+1,False)
                memo[(i,buying)] = max(sell, cooldown)
            return memo[(i,buying)]

        return dfs(0,True)

# Time Complexeity: O(n)
# Space Complexeity: O(n)

'''
Method 
Recursive DFS solution
1. use a boolean to track if on cooldown
2. helper dfs function. 
3. recursive dfs reduced time complexeity due to memoization. 
4, base cases: 
    - i greater than length, then return 0
    - if in memo then return the memo result
5. if you are able to buy: 
    - max of cooldown and buy
6. if you are unabel to buy: 
    - max of sell and cooldown, sell skips a day. 

'''