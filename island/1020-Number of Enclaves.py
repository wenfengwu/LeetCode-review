# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            #get area of this island
            return dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)+1
        
        #eliminate the edge invalid island on each row
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        #eliminate the edge invalid island on each col
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        #traverse each element and the total of area
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    result += dfs(i,j)
                    
        return result