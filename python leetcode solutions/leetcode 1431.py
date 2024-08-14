# leetcode 1431

# Kids With the Number of Candies

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        max_boolean = []
        for candy in candies: 
            if candy + extraCandies >= max_candies: 
                max_boolean.append(True)
            else: 
                max_boolean.append(False)
        return max_boolean

candies = [2,3,5,1,3]
extraCandies = 3 
test = Solution().kidsWithCandies(candies,extraCandies)
print(test)

# Time Complexeity: O(n)
# Space Complexeity: O(1)