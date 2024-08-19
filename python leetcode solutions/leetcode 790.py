# leetcode 790 

# Tiling Dominos and Trominos

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7 
        if n == 1:
            return 1
        if n == 2: 
            return 2
        if n == 3:
            return 5
        T1, T2, T3 = 1, 2, 5 
        for i in range(4,n+1): 
            T1, T2, T3 = T2, T3, 2*T3 + T1
        return T3 % MOD

        

# O(n) Time Complexeity
# O(1) Space Complexeity

# recurrence relation: T(N) = 2*T(N-1) + T(N-3)
'''
To Fully understand this problem draw out: 
n = 1 - 6 to get the pattern. 
'''