# leetcode 605

# Can Place Flowers.

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        counter = 0 
        if n == 0: 
            return True
        if len(flowerbed) == 1: 
            if flowerbed == [0]:
                return 1 == n

        for i in range(len(flowerbed)):
            if (i == 0 and 
                flowerbed[i] == 0 and 
                flowerbed[i+1] == 0):
                flowerbed[i] = 1 
                counter += 1  

            elif (i == len(flowerbed) -1 and 
                flowerbed[i] == 0 and 
                flowerbed[i-1] == 0):
                flowerbed[i] = 1 
                counter += 1

            elif (flowerbed[i] == 0 and 
                  flowerbed[i-1] == 0 and 
                  flowerbed[i+1] == 0):
                flowerbed[i] = 1 
                counter += 1  
        return counter >= n
# Time Complexeity: O(N)
# Space Complexeity: O(1)
    
        
flowerbed = [0,0,0,0,1]
n = 1 
test = Solution().canPlaceFlowers(flowerbed,n)
print(test)