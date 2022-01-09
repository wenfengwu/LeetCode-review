# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# 给一个升序数组，生成一个平衡二叉搜索树。平衡二叉树定义如下：

# 它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

# 二叉搜索树定义如下：

# 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
# 任意节点的左、右子树也分别为二叉查找树；
# 没有键值相等的节点。
# 平衡二叉树，既然要做到平衡，我们只要把根节点选为数组的中点即可。

# 综上，和之前一样，找到了根节点，然后把数组一分为二，进入递归即可。注意这里的边界情况，包括左边界，不包括右边界。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.addNode(nums, 0, len(nums) - 1)
        
    def addNode(self, nums, start, end):
        if start <= end:
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = self.addNode(nums, start, mid-1)
            node.right = self.addNode(nums, mid + 1, end)
            return node