# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01
# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation: 
# row 1: 0
# row 2: 01
 

# Constraints:

# 1 <= n <= 30

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #base case
        if n == 1:
            return 0
        #get the parent, it is located on n-1 level, and ceil(k/2) location
        previous = self.kthGrammar(n-1, ceil(k/2))
        #check the k is on odd or even location
        kOdd = k%2 == 1
        #if its parent is 1, means 1 --> 10, k==1 if k is odd, otherwise k==0
        if previous == 1:
            return 1 if kOdd else 0
        #if its parent is 0, means 0 --> 01, k==0 if k is odd, otherwise k==1
        else:
            return 0 if kOdd else 1