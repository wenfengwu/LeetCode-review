# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:

# Input: l1 = [0], l2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1= ""
        s2 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
            
        s1 = int(s1)
        s2 = int(s2)
        
        result = str(s1 + s2)
        newHead = ListNode(int(result[0]))
        ruuner = newHead
        left = 1
        while left < len(result):
            ruuner.next = ListNode(int(result[left]))
            left += 1
            ruuner = ruuner.next
        
        return newHead