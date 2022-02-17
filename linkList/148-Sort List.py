# Given the head of a linked list, return the list after sorting it in ascending order

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        arr = []
        runner = head
        
        while runner:
            arr.append(runner.val)
            runner = runner.next
            
        arr = sorted(arr)
        runner = head = ListNode(arr[0])
        
        for i in range(1, len(arr)):
            runner.next = ListNode(arr[i])
            runner = runner.next
        
        return head