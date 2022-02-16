# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        
        runner = head
        arr = []
        
        while runner:
            arr.append(runner.val)
            runner = runner.next
        
        left = 1
        right = len(arr) - 1
        
        head.next = None
        runner = head
        
        while left < right:
            runner.next = ListNode(arr[right])
            right -= 1
            runner = runner.next
            runner.next = ListNode(arr[left])
            left += 1
            runner = runner.next
            if left == right:
                runner.next = ListNode(arr[left])

            
        return head
            