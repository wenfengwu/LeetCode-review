# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res
    
    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)