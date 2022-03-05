# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        result = []
        
        if root:
            q.append(root)
            
        while q:
            subRes = []
            size = len(q)
            
            while size > 0:
                current = q.popleft()
                size -= 1
                subRes.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                
            result.append(subRes)
        
        return result[::-1]