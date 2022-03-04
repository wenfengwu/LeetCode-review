# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         if len(candidates) == 0:
#             return
#         #sort the array first
#         candidates.sort()
#         result = []
        
#         def dfs(start, subRes, total, target):
#             #found the sub result
#             if total == target:
#                 #add in the copy of subRes to result
#                 result.append(subRes.copy())
#                 return
#             #if total greater than target, return
#             if total > target:
#                 return
#             prev = -1
#             #enumerate each posibility, call the dfs function recursively
#             for i in range(start, len(candidates)):
#                 if candidates[i] == prev:
#                     continue
#                 subRes.append(candidates[i])
#                 total += candidates[i]
#                 dfs(i+1, subRes, total, target)
#                 total -= candidates[i]
#                 subRes.pop()
#                 prev = candidates[i]
                
#         dfs(0, [], 0, target)
        
#         return result

        candidates.sort()
        result = []
        
        def dfs(cur, start, total):
            if total == 0:
                result.append(cur.copy())
                return
            if total < 0 or start >= len(candidates):
                return
            
            prev = -1
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                cur.append(candidates[i])
                dfs(cur, i+1, total-candidates[i])
                cur.pop()
                prev = candidates[i]
                
        dfs([], 0, target)
        
        return result
    