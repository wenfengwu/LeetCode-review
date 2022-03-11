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
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        visited = set()
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        q = deque()
        q.append([0,0,1])
        visited.add((0,0))
        
        while q:
             for _ in range(len(q)):
                    r, c, d = q.popleft()
                    if r == n-1 and c == n-1:
                        return d
                    for i, j in dirs:
                        nr = r + i
                        nc = c + j
                        if 0 <= nr < n and 0 <= nc < n:
                            if (nr,nc) not in visited and grid[nr][nc] == 0:
                                q.append([nr, nc, d + 1])
                                visited.add((nr,nc))
            
            
        return -1
                    
        