# leetcode 76 

# Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        
        window = {}
        count = {}
        for c in t: 
            count[c] = 1 + count.get(c,0)
        
        l, res = 0, ""
        req, cur = len(count), 0
        for r in range(len(s)): 
            c = s[r] 
            window[c] = 1 + window.get(c,0)

            if c in count and window[c] == count[c]: 
                cur +=1

            while req == cur: 
                if res == '' or  r - l + 1 < len(res): 
                    res = s[l:r+1]
                window[s[l]] -= 1
                
                if s[l] in count and window[s[l]] < count[s[l]]:
                    cur -=1
                l += 1
        return res

# Time Complexeity: O(n + m)
# Space Complexeity: O(n + m)

'''
Method: 
Sliding window algorithm. 
1. create 2 hashmaps, one for window and one for count in string t.
2. add all of t to count
3. add iterate with right pointer add element to r
4. update current count and window as needed. 
5. when cur == req, shrink window on the left side until condition no longer met. 
6. append new result if shorter than the current result. 
7. is a requirement is removed during incrementing left pointer then reduce cur value. 
'''

# below is my less efficient first implementation. 
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = set(t)
        dict = Counter(t)

        res = ''
        l, r = 0,1
        if s[l] in chars: 
            dict[s[l]] -= 1 
            if dict[s[l]] == 0:
                del dict[s[l]]
        if dict == {}: 
            return s[0]
        
       
        while r < len(s): 
            if s[r] in chars: 
                dict[s[r]] -= 1 
            if all(value  <= 0 for value in dict.values()): 
                while all(value  <= 0 for value in dict.values()): 
                    if s[l] in chars: 
                        dict[s[l]] += 1
                    l += 1
                if res == '' or ((r+1) - (l-1)) < len(res):  
                    res = s[l-1:r+1]
            r += 1


        return res
s = "ADOBECODEBANC"
t = 'ABC'
test = Solution().minWindow(s,t)
print(test)





                

            
            
                 



        