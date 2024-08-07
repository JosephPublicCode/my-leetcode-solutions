# leetcode 74 

# search in a Matrix

# binary search in a 2D matrix

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        l,r = 0, m*n - 1

        while l <= r: 
            mid = l + (r - l) // 2
            h = mid % n
            v = mid // n 
            if target == matrix[v][h]:
                return True
            elif target > matrix[v][h]:
                l = mid + 1 
            elif target < matrix[v][h]:
                r = mid - 1 
        return False
    
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1,2]]
target = 3 
test = Solution().searchMatrix(matrix,target)
print(test)

# Time Complexeity: O(log n)
# Space Complexeity: O(1)

'''
Method: 

Standard Binary Search

just requires position manipulation using modulus and integer division.

'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
            rows, cols = len(matrix), len(matrix[0])
            top, bot = 0, rows - 1 

            # finding the row the solution is between.
            while top <= bot: 
                row = (bot) + (top - bot)//2
                if target > matrix[row][-1]:
                    top = row + 1 
                elif target < matrix[row][0]:
                    bot = row - 1 
                else:
                    break

            if not (top <= bot):
                return False
            row = bot + (top - bot)//2 
            l,r = 0, cols -1
            # binary search on the correct row.
            while l <= r:
                m = l + (r-l)//2 
                print(l,r,m)
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]:
                    r = m - 1 
                else: 
                    return True
            return False
    
