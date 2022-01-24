# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        #if n is the length of the linklist, the delete node will be the head, so return head.next
        if fast == None:
            return head.next
        #locate the slow pointer to the node before the delete node
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        #reassign the pointer, means delete the node
        slow.next = slow.next.next
        return head