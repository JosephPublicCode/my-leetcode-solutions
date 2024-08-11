# leetcode 739

# Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: 
                        list[int]) -> list[int]:
        stack = [] 
        index = []
        counts = [0 for _ in range(len(temperatures))]
        for i,t in enumerate(temperatures): 
            while stack and stack[-1] < t:
                stack.pop()
                ind = index.pop()
                counts[ind] = i - ind
            stack.append(t)
            index.append(i)
        return counts
# O(N) time complexeity
# O(N) memory complexeity

'''
Method: 
use of a min stack.
1. initialize a stack and index list and a counts list. 
2. only add to the stack and index if the stack is empty of the end element is less than the current. 
3. when we encounter a larger temperature we continue to pop until larger or empty.
4. as we pop update the counts[ind] = current temp position - popped position. 
'''



def dailyTemperatures(self, temperatures: 
                        list[int]) -> list[int]:
        stack = [] 
        counts = [0 for _ in range(len(temperatures))]
        for i,t in enumerate(temperatures): 
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop()
                counts[stackInd] = i - stackInd
            stack.append([t,i])
            return counts



temperatures = [23,24,25,21,19,22,26,23]
test = Solution().dailyTemperatures(temperatures)
print(test)
            