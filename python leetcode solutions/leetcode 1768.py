# leetcode 1768 

# merge alternative characters in strings

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        res = ''
        i = 0 
        while i < min_len: 
            res += word1[i]
            res += word2[i]
            i += 1
        while i < len(word1): 
            res += word1[i]
            i += 1
        while i < len(word2): 
            res += word2[i]
            i += 1
        return res
    
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        res = ''
        i = 0 
        for i in range(min_len):  
            res += word1[i]
            res += word2[i]
        return res + word1[i+1:] + word2[i+2:]