

class Solution:
    def compress(self, chars: list[str]) -> int:
        l, r = 0,0

        while r < len(chars): 
            char = chars[r]
            count = 0

            while r < len(chars) and chars[r] == char: 
                r += 1 
                count += 1 
            chars[l] = char
            l += 1 

            if count > 1: 
                for i in str(count): 
                    chars[l] = i
                    l +=1
        return l
# O(N) Time Complexeity
# O(1) Space Complexeity

chars = ['a','a','b','b','c','c','c']
test = Solution().compress(chars)
print(test)