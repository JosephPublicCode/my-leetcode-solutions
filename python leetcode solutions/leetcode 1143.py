# leetcode 1143

# longest common subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)  
        matrix = [[0]*(m+1) for _ in range(n+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else: 
                    matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])
        return matrix[n-1][m-1]
    
# O(n*m) Time Complexeity
# O(n*m) Space Complexeity
'''
Method: 
1. use a matrix in a top or bottom down approach
2. initialise the matrix with one row and column of padding
3. for loops on both strings. 
4. if elements eual then previous + 1 to indicate length
5. else take max of adjacent cells. 


further below is a memoization recursive solution. 
In theory, memoization recursion has the same time and space complexeity as the dp approach. 
However, in practise computers are slower at recursion so they tend to run slower due to: 
- increased overhead
- many redundant function calls
'''

class Solution: 
    def longestCommonSubsequence(self,text1:str,text2:str) -> int: 
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1 
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
    
text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
test = Solution().longestCommonSubsequence(text1,text2)
print(test)

# Memoization
# O(n*m) Time Complexeity
# O(n*m) Space Complexeity
class Solution: 
    def longestCommonSubsequence(self,text1:str,text2:str) -> int: 
        memo = {}

        def lcs(i,j): 
            if (i,j) in memo: 
                return memo[(i,j)]
            if i == len(text1) or j == len(text2): 
                return 0
            
            if text1[i] == text2[j]: 
                memo[(i,j)] =  1 + lcs(i+1,j+1)
            else: 
                memo[(i,j)] = max(lcs(i+1,j),lcs(i,j+1))
            return memo[(i,j)]            
        
        return lcs(0,0)
    
text1 = "abcde"
text2 = "ace"
test = Solution().longestCommonSubsequence(text1,text2)
print(test)