# leetcode 150

# Evalulate Reverse Polish Notation




class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens: 
            if token in ["+","-","/","*"]:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(num1+num2)
                if token == "-":
                    stack.append(num2 - num1)
                if token == "/":
                    stack.append(int(num2/num1))
                if token == "*":
                    stack.append(num2*num1)
            else: 
                stack.append(int(token))
        return stack.pop()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
test = Solution().evalRPN(tokens)
print(test)

# Time complexeity: O(n)
# Space complexeity: O(n)

'''
Method: 
use a stack data structure. 
1. add numbers to the stack
2. operations pop two items from the stack and perform the computation and then add the value back to the stack. 

'''
