# leetcode 2390

# Removing Stars from a String

class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        l = len(s)

        for i in range(l): 
            if res and  s[i] == "*": 
                res = res[:-1]

            else: 
                res += s[i]
        return res



s = "erase*****"
test = Solution().removeStars(s)
print(test)

# Time Complexeity: O(n)
# Space Complexeity: O(n)



# alternative - create a list and then join the list together. 
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        l = len(s)

        for i in range(l): 
            if res and  s[i] == "*": 
                res.pop()

            else: 
                res.append(s[i])
        return ''.join(res)