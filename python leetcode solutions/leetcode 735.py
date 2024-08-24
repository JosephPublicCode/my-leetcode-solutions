# leetcode 735 

# Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids: 
            while stack and asteroid < 0 < stack[-1]: 
                if stack[-1] < abs(asteroid): 
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid): 
                    stack.pop()
                break
            else: 
                stack.append(asteroid)
        return stack

# Time Complexeity: O(n)
# Space Complexeity: O(n)


'''
Method: 
Use a stack data structure. 
1. iterate through the asteroids
2. while we have a stack and asteroid is less than 0 and top of stack is greater than 0
3. this means a collisions will occur
    - if equal asteroids then stack pop and break
    - else current asteroid is larger than stack so pop from stack and continue
4. else case append the current asteroid to the stack 
5. return the stack. 


'''

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        copy = asteroids
        stack = []
        cur = copy.pop(0)
        stack.append(cur)

        while copy: 
            cur = copy.pop(0)
      
            if not stack: 
                stack.append(cur)
                continue
            while stack:

                if (stack[-1] < 0) or (stack[-1] > 0 and cur > 0): 
                    stack.append(cur)
                    break

                elif abs(stack[-1]) == abs(cur): 
                    stack.pop()
                    break

                elif abs(stack[-1]) < abs(cur): 
                    stack.pop()
                    if not stack: 
                        stack.append(cur)
                        break 
                else: break
                
        return stack
    
asteroids = [1,-1,-2,-2]
test = Solution().asteroidCollision(asteroids)
print(test)


