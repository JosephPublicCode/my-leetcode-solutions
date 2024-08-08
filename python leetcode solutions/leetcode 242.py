# leetcode 242 
# valid anagram
from collections import Counter
# Algorithm

''' 
A number of different approaches are given below: 

the easiest is a hashmap approach as seen directly below: 
This has O(N) time and O(N) space

'''
class Solution: 
    def isAnagram(self,s:str,t:str): 
        if len(s) != len(t): 
            return False
        countS, countT = {},{}
        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[s[i]] = 1 + countT.get(s[i],0)
        for c in countS: 
            if countS[c] != countT.get(c,0): 
                return False
        return True

# longer hashmap


class Solution:
    def isAnagram(self,s:str,t:str) -> bool: 
        if len(s) != len(t): 
            return False
        shashmap = {}
        thashmap = {}
        for i in s: 
            if i in shashmap: 
                shashmap[i] +=1
            else:
                shashmap[i] = 1 
        for j in t: 
            if j in thashmap: 
                thashmap[j] +=1
            else:
                thashmap[j] = 1 
        return shashmap == thashmap

s= 'anagram'
t = 'naafrma'
test = Solution().isAnagram(s,t)
print(test)

class Solution:
    def isAnagram(self,s:str,t:str) -> bool: 
        if len(s) != len(t): 
            return False
        else: 
            x = set(s)
            for i in x:
                if s.count(i) != t.count(i):
                    return False
        return True

s= 'anagram'
t = 'naafrma'
test = Solution().isAnagram(s,t)
print(test)

# O(n) time complexeity and hashmap means O(n) space complexeity

class Solution: 
    def isAnagram(self,s:str,t:str): 
        return Counter(s) == Counter(t)
    # import the collections module to get the counter data structure.


# O(nlogn) time complexeity and O(1) space complexeity

class Solution: 
    def isAnagram(self,s:str,t:str): 
        if len(s) != len(t): 
            return False
        return sorted(s) == sorted(t)
s= 'anagram'
t = 'naagrma'
test = Solution().isAnagram(s,t)
print(test)
