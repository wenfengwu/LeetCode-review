# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]

# Input: head = [1,2,null,3]
# Output: [1,3,2]

# Input: head = []
# Output: []

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head:
            runner = head
            stack = []
            #edge case[1, null, 2, null, 3, null]
            while runner:
                if runner.child != None:
                    if runner.next != None:
                        stack.append(runner.next)
                    runner.next = runner.child
                    runner.child.prev = runner
                    runner.child = None
                #if runner goes the last node, break
                if runner.next == None and runner.child == None:
                    break
                
                runner = runner.next

            while len(stack) > 0:
                connect = stack.pop()
                runner.next = connect
                connect.prev = runner

                while runner.next:
                    runner = runner.next
        
        return head