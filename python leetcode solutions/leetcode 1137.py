# leetcode 1137

# N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: 
            return 0 
        if n == 1 or n == 2: 
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = dp[2] = 1 
        for i in range(3,n+1): 
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
# O(n) Time Complexeity
# O(n) Space Complexeity


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: 
            return 0 
        if n == 1 or n == 2: 
            return 1
        t1, t2, t3 = 0, 1, 1
        for i in range(3,n+1):
            t1, t2, t3 = t2,t3,t3+t2+t1
        return t3  
# O(1) Time Complexeity
# O(n) Space Complexeity

'''
can also be done with: 
recursion: O(2^N)
recursion with memoization: O(N)
'''