# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).

# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
 

# Constraints:

# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = 0
        
        #dfs function to check island
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            
            if grid[i][j] == 1:
                return
            
            grid[i][j] = 1
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        #eliminate the edge invalid inlands
        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)
        
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        #traverse each valid postion and get the numbers of islands
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    result += 1
                    dfs(i,j)
        return result