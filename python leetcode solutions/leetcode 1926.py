# leetcode 1926

# Nearest Exit from Entrance in Maze

from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        cols, rows = len(maze[0]),len(maze)
        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        visit = set()
        q.append((entrance[0],entrance[1],0))
        visit.add((entrance[0],entrance[1]))
        
        while q: 
            r, c, steps = q.popleft()

            if (r == 0 or r == (rows - 1) or \
                c == 0 or c == (cols -1 ))\
                and [r,c] != entrance: 
                return steps


            for dr, dc in dir: 
                r_d = r + dr
                c_d = c + dc

                if 0 <= r_d <= rows - 1 and\
                    0 <= c_d <= cols - 1 and\
                    (r_d,c_d) not in visit and\
                        maze[r_d][c_d] == '.': 
                    q.append((r_d, c_d, steps + 1))
                    visit.add((r_d,c_d))
        return -1
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

test = Solution().nearestExit(maze,entrance)
print(test)

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
test = Solution().nearestExit(maze,entrance)
print(test)
# Time Complexeity: O(rows*cols)
# Space Complexeity: O(rows*cols)

'''
Method: 
BFS with a queue can change the base maze or use a visit set for tracking. 
1. define the queue and visit set
2. append the entrance to the queue
3. while q run algo
4. if at an edge and not the entrance then return the number of steps to get there
5. for all neighbors, check that it is open and in range of possible values then append to the queue and visit set. 

'''

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        cols, rows = len(maze[0]),len(maze)
        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        visit = set()
        q.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]] == '+'
        
        while q: 
            r, c, steps = q.popleft()

            if (r == 0 or r == (rows - 1) or \
                c == 0 or c == (cols -1 ))\
                and [r,c] != entrance: 
                return steps


            for dr, dc in dir: 
                r_d = r + dr
                c_d = c + dc

                if 0 <= r_d <= rows - 1 and 0 <= c_d <= cols - 1 and maze[r_d][c_d] == '.': 
                    q.append((r_d, c_d, steps + 1))
                    maze[r_d][c_d] = '+'
        return -1