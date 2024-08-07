# leetcode 202 

# The Happy Number problem. 


class Solution:
    def isHappy(self, n: int) -> bool:
        previousValues = {}
        iteratedValue = n
        currentValue = 0
        while currentValue != 1: 
            currentValue = 0
            while iteratedValue != 0: 
                remainder =iteratedValue % 10 
                currentValue += (remainder)**2
                iteratedValue = iteratedValue // 10
            if currentValue in previousValues: 
                return False
            iteratedValue = currentValue
            previousValues[currentValue] = currentValue
        return True   
test = Solution().isHappy(7)
print(test)

# Time Complexeity: O(n)
# Space Complexeity: O(n)


'''
Method: 

1. while current value is not equal to 1
2. remainder using modulus and square it and append to current value. 
3. continue using integer division until no iterated value left. 
4. if the number has already been seen in the hashmap 
then the value is in an infinite loop and return false.
'''

# same as above just using a helper function

#  Alternative Solution
class Solution:
    def isHappy(self, n: int) -> bool:
        visits = set()

        while n not in visits: 
            visits.add(n)
            n = self.sum_of_squares(0)

            if n == 1: 
                return True
            
        return False
    
    def sum_of_squares(self,n:int) -> int: 
        square_sum = 0 
        while n: 
            square_sum += (n%0)**2
            square_sum = square_sum // 10
        return square_sum







        
