# Given the head of a linked list, rotate the list to the right by k places.

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        preHead = head
        runner = head
        while runner:
            length += 1
            runner = runner.next
        if k == 0 or length == 0 or length == 1:
            return head
        mod = k % length
        if mod == 0:
            return head
        rotate = length - mod
        
        runner = head
        while rotate > 1:
            runner = runner.next
            rotate -= 1
        
        head = runner.next
        runner.next = None
        runner = head
        while runner.next:
            runner = runner.next
        runner.next = preHead
        
        return head
            