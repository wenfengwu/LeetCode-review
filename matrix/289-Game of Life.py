# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



# Original | New | State
#     0       0       0  
#     1       0       1  
#     0       1       2
#     1       1       3

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def countNeibhors(r, c):
            total = 0
            #check the eight directions
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    #skip itself and the element which out of bounds
                    if (i == r and j == c) or i < 0 or j < 0 or i >= rows or j >= cols:
                        continue
                    if board[i][j] in [1, 3]:
                        total += 1
                        
            return total
        
        for i in range(rows):
            for j in range(cols):
                nei = countNeibhors(i, j)
                if board[i][j] == 1:
                    if nei in [2, 3]:
                        board[i][j] = 3
                #if element is 0
                elif nei == 3:
                    board[i][j] = 2
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1
                    
        return board