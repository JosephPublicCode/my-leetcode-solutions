# leetcode 151

# Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
       
        cur = ''
        words = []

        for char in s: 
            if char == ' ': 
                if cur != '':
                    words.append(cur)
                    cur = ''

            else: 
                cur += char
        if cur != '': 
            words.append(cur)
        words.reverse()

        return ' '.join(words)

s = 'the    sky is blue     green'
test = Solution().reverseWords(s)
print(test)
    

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]

        s = " ".join(s)
        return s
