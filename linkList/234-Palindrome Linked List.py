# Given the head of a singly linked list, return true if it is a palindrome.

# Input: head = [1,2,2,1]
# Output: true

# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # run twice of the slow pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the half linklist
        temp = None
        while slow:
            cur = slow.next
            slow.next = temp
            temp = slow
            slow = cur
        
        # compare each elements
        while temp:
            if temp.val != head.val:
                return False
            temp = temp.next
            head = head.next
        
        return True