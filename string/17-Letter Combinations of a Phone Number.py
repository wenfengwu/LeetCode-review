# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        #make a hashmap for digits to alpha
        dict = {"2" : "abc",
                "3" : "def",
                "4" : "ghi",
                "5" : "jkl",
                "6" : "mno",
                "7" : "qprs",
                "8" : "tuv",
                "9" : "wxyz",}
        
        #backtrack function takes index of digtis, and temp string
        def backTrack(idx, curStr):
            #if length of temp string == length of digits, which is result
            if len(curStr) == len(digits):
                #add whole string to result
                res.append(curStr)
                return
            #iterate each element on dict(digits[idx] gets the number, dict[digits[idx]] get alphas on each number)
            for c in dict[digits[idx]]:
                backTrack(idx+1, curStr + c)
                
            return
        
        #call the function only digits exit
        if digits:
            backTrack(0, "")
            
        return res