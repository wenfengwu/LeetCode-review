# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0]) - 1
        
        #set the starting point to the last index of first row
        #left side always getting small, bottom side always getting bigger 
        while row < len(matrix) and column >= 0:
            #if this element greater than target, then move left
            if matrix[row][column] > target:
                column -= 1
            #if this element less than target, then move down  
            elif matrix[row][column] < target:
                row += 1
            else:
            #found the target, return True
                return True
        #not found return False
        return False