# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# recursion 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        current = root
        self.helper(current.left, current.right)
        return root
    
    def helper(self, node1, node2):
        if node1 == None or node2 == None:
            return
        node1.next = node2
        
        self.helper(node1.left, node1.right)
        self.helper(node2.left, node2.right)
        self.helper(node1.right, node2.left)



# level traverse
class Solution(object):
def connect(self, root):
    if root is None: return None
    dq, pre_level, pre_node = deque([(1, root)]), 0, None
    while dq:
        level, node = dq.popleft()
        if level == pre_level:  # current node is not the first node of level
            pre_node.next = node
            pre_node = node
        else:  # pre_level < level and node is the first node of level, then no need to update pre_node.next, 
            # leave it as None, update pre_node = node only.
            pre_level, pre_node = level, node
        if node.left:  # root is a perfect binary tree, once left exists, right must also exist
            dq.append((level + 1, node.left))
            dq.append((level + 1, node.right))
    return root