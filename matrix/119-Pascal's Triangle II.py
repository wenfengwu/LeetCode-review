# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        
        for i in range(rowIndex):
            pre = [0] + res[-1] + [0]
            temp = []
            for j in range(len(res[-1]) + 1):
                temp.append(pre[j] + pre[j+1])
            res.append(temp)
        return res[-1]