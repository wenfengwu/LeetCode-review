# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
 

# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
# Accepted
# 416,341
# Submissions
# 905,119

"""

                cur = cur.next
            # Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        head = Node()
        headCur = head
        cur = root
        
        while cur:
            while cur:
                if cur.left:
                    headCur.next = cur.left
                    headCur = headCur.next
                if cur.right:
                    headCur.next = cur.right
                    headCur = headCur.next
                
            cur = head.next
            head.next = None
            headCur = head
            
        return root