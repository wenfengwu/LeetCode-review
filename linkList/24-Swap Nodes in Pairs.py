# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if head exist
        if head:
            second = head.next
            #if head.next exist
            if second:
                #swap the nodes
                temp = second.next
                second.next = head
                head.next = temp
                #call itself, change second node
                second.next.next = self.swapPairs(second.next.next)
                #return second node for privious call
                return second
        #if there is no node or only one node, return head node 
        return head