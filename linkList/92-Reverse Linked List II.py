# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #if no reverse range, return ifself
        if left == right:
            return head
        #add a dummy node at front
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        #locate the pre to the front of the left
        for i in range(left - 1):
            pre = pre.next
        
        #set cur to the left node
        cur = pre.next
        #set reverse pointer to Node in order to the first swap round
        reverse = None
        
        #start swapping, reverse pointer will stop at the at the end of the swapped node, next and cur pointers will stop at the next node of right,
        for i in range(right - left + 1):
            nextNode = cur.next
            cur.next = reverse
            reverse = cur
            cur = nextNode
        
        #reconnect the linklist
        pre.next.next = nextNode
        pre.next = reverse
        
        #return the head of linklist
        return dummy.next
        
        