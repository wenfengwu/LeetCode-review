# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows - 1):
            #take the last row and add 0 to the front and back
            previous = [0] + res[-1] + [0]
            temp = []
            for j in range(len(res[-1]) + 1):
                #use two pointer the add element then assign it to temp arr
                temp.append(previous[j] + previous[j+1])
            #append the entire temp array to result array
            res.append(temp)
        return res