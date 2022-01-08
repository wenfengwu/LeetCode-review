# // Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# // Input: root = [1,2,2,3,4,4,3]
# // Output: true

# // Input: root = [1,2,2,null,3,null,3]
# // Output: false

# // Constraints:

# // The number of nodes in the tree is in the range [1, 1000].
# // -100 <= Node.val <= 100

# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode() {}
#  *     TreeNode(int val) { this.val = val; }
#  *     TreeNode(int val, TreeNode left, TreeNode right) {
#  *         this.val = val;
#  *         this.left = left;
#  *         this.right = right;
#  *     }
#  * }
#  */
# class Solution {
#     public boolean isSymmetric(TreeNode root) {
#         if(root == null){
#             return true;
#         }
#         //pass to child to recursion
#         return compare(root.left, root.right);
#     }
    
#     private boolean compare(TreeNode left, TreeNode right){
#         //if both child are null, return null
#         if(left == null && right == null){
#             return true;
#         }
#         //if one of them is null, return false
#         if(left == null || right == null){
#             return false;
#         }
#         //check values are equal and left.right, right.left, and left.left, right.right nodes are equal or not
#         return left.val == right.val && compare(left.right, right.left) && compare(left.left, right.right);
#     }
# }


# python sulution:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
    
        def isMirror(tree1, tree2):
            if not tree1 or not tree2: # if one of them is null
                return tree2 == tree1  # compare them
            if tree1.val != tree2.val: # if above not executed, means they are both number
                return False           # if they are both different return false
                                    # if they are similar go and look further
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        
        return isMirror(root.left, root.right)