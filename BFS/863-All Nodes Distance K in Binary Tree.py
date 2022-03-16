# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Example 2:

# Input: root = [1], target = 1, k = 3
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = {}
        self.getParents(root, None)
        return self.bfs(target, k)
    
    def getParents(self, node: TreeNode, parent: TreeNode) -> None: 
        if node == None: return
        
        self.parent[node.val] = parent
        
        self.getParents(node.left, node)
        self.getParents(node.right, node)
        
    def bfs(self, start: TreeNode, K: int) -> List[int]:
        res, q, visited = [], [(start, 0)], set()
        
        while q:
            n, d = q.pop(0)
            
            if n not in visited:
                if d == K: res.append(n.val)
                visited.add(n)
                
                if n.left: q.append((n.left, d+1))
                if n.right: q.append((n.right, d+1))
                if self.parent[n.val]: q.append((self.parent[n.val], d+1))
                                   
        return res