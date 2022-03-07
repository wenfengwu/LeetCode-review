# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        
        #get the row and column size
        row = len(grid)
        col = len(grid[0])
        
        #define the dfs function
        def dfs(i, j):
            #if i or j out of range, return
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            
            #if current position is sea, return
            if grid[i][j] == '0':
                return
            
            #change the current position to '0', instead of put it into visited array
            grid[i][j] = '0'
            
            #recursively run 4 direction positions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        #traverse all element on the 2D array
        for i in range(row):
            for j in range(col):
                #when it hit the island, increment the result, then call dfs function
                if grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        
        return result