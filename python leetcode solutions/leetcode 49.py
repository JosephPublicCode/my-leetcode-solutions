# leetcode 49

# Group Anagrams


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs: 
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            
            res[tuple(count)].append(s)
        print(res) 
        return res.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]
test = Solution().groupAnagrams(strs)
print(test)

# Time Complexeity: O(n*m)
# Space Complexeity: constant additional space O(N)

'''
Method: 
1. use a dictionary with lists as keys
2. for all the different strings record their counts of each letter using ord to define their position in the count list. 
3. append the key to the tuple of the count list. 
4. return the values of the dictionary. 


'''

# alternative, sort all of the words.
# Time Complexeity:  O(n*mlogn)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs: 
            res["".join(sorted(s))].append(s)
        return res.values()
strs = ["eat","tea","tan","ate","nat","bat"]
test = Solution().groupAnagrams(strs)
print(test)

