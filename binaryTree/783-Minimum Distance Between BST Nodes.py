# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.


# Input: root = [4,2,6,1,3]
# Output: 1

# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def helper(current, lowVal, highVal):
            if not current:
                return highVal - lowVal
            left = helper(current.left, lowVal, current.val)
            right = helper(current.right, current.val, highVal)
            return min(left, right)
        return helper(root, float('-inf'), float('inf'))

# 需要用递归来传值，我们只需要中序遍历这个二叉树，把每个节点的值传到数组，我们得到的就是一个从小到大排好序的数组。然后在数组内比较相邻两个数的差值，最后返回最小值就可以了