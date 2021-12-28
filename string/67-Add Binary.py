# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


# int(a, 2) casting string to int as binary
# The int() function converts the specified value into an integer number.

# The int() function returns an integer object constructed from a number or string x, or return 0 if no arguments are given.

# add them together and cast the to binary 

# output will be 0b101101 
# the elements after the second index is what we need, out sum[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a,2) + int(b,2))
        return sum[2:]


