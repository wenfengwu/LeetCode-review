# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = self.preorder(p, [])
        res2 = self.preorder(q, [])
        return res1 == res2
    
    def preorder(self, root, arr):
        if not root:
            arr.append(None)
        else:
            arr.append(root.val)
            self.preorder(root.left, arr)
            self.preorder(root.right, arr)
        return arr


#Solution 02
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both are None, true
        if not p and not q:
            return True
        #if either one side is None, false
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)