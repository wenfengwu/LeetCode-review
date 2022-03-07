# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        
        #mark all valid region to 'T'
        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            #if board[i][j] == "X" or board[i][j] == "T":
            if board[i][j] != 'O':
                return
            board[i][j] = "T"
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        #mark all valid region on boundary to 'T'    
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
            
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        #change all bounded 'O' to 'X' and restore all 'T' back to 'O'
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        