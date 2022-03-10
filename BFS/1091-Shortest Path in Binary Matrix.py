# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
    
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        seen = set()
        queue = collections.deque([(0,0,1)]) # indice, dist
        seen.add((0,0))
        
        while queue:
          i,j,dist = queue.popleft()
          if i == n -1 and j == n - 1:
            return dist
          for d1, d2 in dirs: 
            x, y = i + d1, j + d2
            if 0 <= x < n and 0 <= y < n:
                
              if (x,y) not in seen and grid[x][y] == 0:
                seen.add((x, y))
                queue.append((x, y, dist + 1))
        return -1
                    
        