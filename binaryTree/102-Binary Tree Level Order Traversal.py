# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS solution deep first solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        result = []
        self.dfs(root, result, 0)
        return result
    
    def dfs(self, root, result, level):
        if root == None:
            return
        if len(result) < level + 1:
            result.append([])
        result[level].append(root.val)
        self.dfs(root.left, result, level + 1)
        self.dfs(root.right, result, level + 1)


# BFS solution breadth first solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        result = []
        if root:
            q.append(root)
        while q:
            newlist = []
            size = len(q)
            
            while size > 0:
                current = q.popleft()
                newlist.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                size -= 1
                
            result.append(newlist)
        
        return result
        