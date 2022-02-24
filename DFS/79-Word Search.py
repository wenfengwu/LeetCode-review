# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #get the row and coloumn of the matrix
        rows, cols = len(board), len(board[0])
        #visited map
        visited = set()
        
        #depth first search
        def dfs(r, c, match):
            if match == len(word):
                return True
            #if does not match either one, return false, out of bound or word does not match, or already visited
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[match] != board[r][c] or (r,c) in visited):
                return False
            #put the visted word in to set
            visited.add((r, c))
            #go to four direction
            res = (dfs(r + 1, c, match + 1) or dfs(r - 1, c, match + 1) or
                   dfs(r, c + 1, match + 1) or dfs(r, c - 1, match + 1))
            #remove the visted positon for next recursion
            visited.remove((r,c))
            return res
        
        #go to each position then call the dfs funtion
        for i in range(rows):
            for j in range(cols):
                #if find anyone one path match the word, return true
                if dfs(i, j, 0):
                    return True
        
        #else, return false
        return False
                    
        