# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.



# set a bound, left < target.val < right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        return self.valid(root, -sys.maxsize, sys.maxsize)
    
    def valid(self, root, left, right):
        if root == None:
            return True
            
        if(root.val <= left):
            return False
        if(root.val >= right):
            return False
        
        return self.valid(root.left, left, root.val) and self.valid(root.right, root.val, right)