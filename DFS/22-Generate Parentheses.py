# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        result = []
        
        def dfs(left, right, subRes):
            #if left Parentheses is more than right Parentheses, it is illegal
            if right < left:
                return
            #if one of the Parentheses less than 0, it is illegal
            if left < 0 or right < 0:
                return
            #if the both got 0, we have a legal sub result
            if left == 0 and right == 0:
                result.append(subRes)
                return
            
            #try to add one left Parentheses
            subRes += '('
            dfs(left-1, right, subRes)
            subRes = subRes[:-1]

            #try to add one right Parentheses
            subRes += ')'
            dfs(left, right-1, subRes)
            subRes = subRes[:-1]
            
        dfs(n, n, "")
        
        return result
            