# leetcode 79

# word search 

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        COLS, ROWS = len(board[0]), len(board)
        path = set()
        def dfs(i, row, col):

            if i == len(word): 
                return True
            if ((row < 0 or row == ROWS) or 
                (col < 0 or col == COLS) or 
                (board[row][col] != word[i]) or 
                (row,col) in path):
                return False

            path.add((row,col))

            res = (dfs(i+1,row+1,col) and
            dfs(i+1,row-1,col) and
            dfs(i+1,row,col+1) and
            dfs(i+1,row,col-1) )
            path.remove((row,col))

            return res
            

            

        for col in range(COLS):
            for row in range(ROWS): 
                if dfs(0,row,col): 
                    return True
        return False
    
# Time Complexeity: O(N^4)
# Space Complexeity: O(N)
'''
Method: Recursive Backtracking DFS

1. dfs helper function, checks if: 
        Base Case 1 
            - the row and column values are in the range of the matrix
            - the value has already been visited
            - the value in the board is equal to the current word value
        Base Case 2
            - end of word is exceeded meaning that you have success
2. dfs in all 4 directions. 
3. run the dfs for all positions in the matrix. 

'''

    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCB"

test = Solution().exist(board,word)
print(test)

# alternative solution with list slicing. 
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        COLS, ROWS = len(board[0]), len(board)
        path = set()
        def dfs(word, row, col):
            if (not word or
                (row < 0 or row == ROWS) or 
                (col < 0 or col == COLS) or 
                (board[row][col] != word[0]) or 
                (row,col) in path):
                return False
            if len(word) == 1 and \
                board[row][col] == word[0]: 
                return True

            path.add((row,col))

            res = (dfs(word[1:],row+1,col) or
            dfs(word[1:],row-1,col) or
            dfs(word[1:],row,col+1) or
            dfs(word[1:],row,col-1) )
            path.remove((row,col))

            return res
            

            

        for col in range(COLS):
            for row in range(ROWS): 
                if dfs(word,row,col): 
                    return True
        return False
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCB"

test = Solution().exist(board,word)
print(test)