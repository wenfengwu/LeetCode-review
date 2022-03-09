# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        result = 0
        row = len(grid)
        col = len(grid[0])
        
        #determite which is island and get their area
        def dfs(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return 0
            
            if grid[i][j] == 0:
                return 0
            #change 1 to 0 instead of double checking
            grid[i][j] = 0
            
            #return the area of this island
            return dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)+1
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    #get the largest area
                    result = max(result, dfs(i,j))
        
        return result