# leetcode 994

# Rotting Oranges

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        t = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        while q:
            i, j, t = q.popleft()

            if i > 0 and grid[i-1][j] == 1:
                q.append((i-1,j,t+1))
                grid[i-1][j] = 2

            if i < m -1 and grid[i+1][j] == 1:
                q.append((i+1,j,t+1))
                grid[i+1][j] = 2

            if j > 0 and grid[i][j-1] == 1:
                q.append((i,j-1,t+1))
                grid[i][j-1] = 2
                
            if j < n - 1 and grid[i][j+1] == 1:
                q.append((i,j+1,t+1))
                grid[i][j+1] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return t
        

grid = [[2,1,1],[1,2,0],[2,1,1]]
test = Solution().orangesRotting(grid)
print(test)


# O(n*m) time and memory


from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        time, fresh = 0,0

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == len(grid) or
                        col < 0 or col ==len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

