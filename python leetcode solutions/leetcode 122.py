# leetcode 122

# Best Time to Buy and Sell a stock II


class Solution: 
    # simpler solution
    def maxProfit(self, prices: list[int]) -> int:
        i,profit = 0,0
        for num in range(prices): 
            if i < len(prices) and num < prices[i+1]: 
                profit = profit + prices[i+1] - num
            i +=1 
        return profit

# Time Complexeity: O(N)
# Space Complexeity: O(1)

'''
Method:
greedy algorithm approach. 
just take profit every time the current number is less than the next number. 


'''
    