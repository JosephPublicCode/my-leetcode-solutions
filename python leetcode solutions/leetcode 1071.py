# leetcode 1071 

# Greatest Common Divisor of Strings
class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        min_len = min(l1,l2) 

        def divisor(i):
            if l1 % i or l2 % i: 
                return False
            f1, f2 = l1//i, l2//i
            return str1[:i]*f1 == str1 and str1[:i]*f2 == str2

        for i in range(min_len,0,-1):
            if divisor(i):
                return str1[:i]
        return ''

       
# Time Complexeity: O(min(n,m))*O(m+n)
# Space Complexeity: O(1)
test = Solution().gcdOfStrings("LEET",'CODE')
print(test)

# greedy approach