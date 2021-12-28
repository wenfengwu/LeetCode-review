# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 4:

# Input: matrix = [[3,6],[7,1],[5,2],[4,8]]
# Output: []
# Explanation: There is no lucky number.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_list = []
        for row in matrix:
            print(row)
            min_list.append(min(row))
            print(min_list)
        
        result = []
        # 将每一列转换成每一行
        for col in zip(*matrix):
            print(col)
            max_num = max(col)
            if max_num in min_list:
                result.append(max_num)
            
        return result