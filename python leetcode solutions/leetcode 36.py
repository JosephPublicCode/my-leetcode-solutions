# leetcode 36

# Valid Sudoku


from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        for i in range(9): 
            for j in range(9):
                val = board[i][j]
                if val.isalnum():
                    k = i // 3 * 3 + j//3
                    if val in row[i] or val in col[j] or val in grid[k]: 
                        return False
                    else: 
                        row[i].add(val)
                        col[j].add(val)
                        grid[k].add(val)
        return True
    
matrix = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
test = Solution().isValidSudoku(matrix)
print(test)

# O(9^2) Time Complexeity
# O(3*9^2) Space Complexeity

'''
Method: 

Use hashsets for: rows, cols and grids. 
1. setup the hashsets
2. locate the value on the board with 2 pointers. 
3. check if alpha numeric. 
4. get grid number using int divisin. 
5. check all validities and if not value return false. 
6. add the value to the row, col and grid. 


'''

# slightly different implementation of the same code
# does not use the alphanumeric function. 
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                else: 
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        return True


# My First Implementation. 
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9): 
            row = set()
            for j in range(9):
                if board[i][j] == '.': 
                    pass
                elif board[i][j] in row: 
                    return False
                else: 
                    row.add(board[i][j])

        
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] == '.': 
                    pass
                elif board[j][i] in col: 
                    return False
                else: 
                    col.add(board[j][i])

        for i in range(3):
            for j in range(3): 
                grid = set()
                for k in range(3*i,3*i + 3): 
                    for l in range(3*j,3*j + 3): 
                        if board[k][l] == '.': 
                            pass
                        elif board[k][l] in grid: 
                            return False
                        else: 
                            grid.add(board[k][l])
        return True
    
matrix = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
test = Solution().isValidSudoku(matrix)
print(test)