# leetcode 1207

# Unique Number of Occurences
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occur = defaultdict()
        for i in arr: 
            if i in occur: 
                occur[i] += 1 
            else: 
                occur[i] = 1 

        if len(occur.values()) == len(set(occur.values())): 
            return True
        return False
    
arr = [1,2,2,1,1,3]
test = Solution().uniqueOccurrences(arr)
print(test)

from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occur = defaultdict()
        for i in arr: 
            if i in occur: 
                occur[i] += 1 
            else: 
                occur[i] = 1 

        return len(occur.values()) == len(set(occur.values()))