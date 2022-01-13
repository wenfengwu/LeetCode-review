# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        
        #postOrder traverse
        self.flatten(root.left)
        self.flatten(root.right)
        
        #get the left and right subtree
        left = root.left
        right = root.right
        
        #make left subtree to be none, and rigth subtree be left
        root.left = None
        root.right = left
        
        #make a temp pointer
        p = root
        
        #traverse current root to the very right subtree
        while p.right != None:
            p = p.right
        
        #assign vert right subtree to be right
        p.right = right