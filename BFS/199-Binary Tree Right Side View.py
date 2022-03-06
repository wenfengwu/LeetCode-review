# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        q = deque()
        
        if root:
            q.append(root)
        result = []
        
        while q:
            size = len(q)
            val = -1000
            while size > 0:
                current = q.popleft()
                size -= 1
                val = current.val
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            result.append(val)
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        q = deque()
        
        if root:
            q.append(root)
        result = []
        
        while q:
            size = len(q)
            head = q[0]
            for i in range(size):
                current = q.popleft()
                if current.right:
                    q.append(current.right)
                if current.left:
                    q.append(current.left)
            result.append(head.val)
        return result