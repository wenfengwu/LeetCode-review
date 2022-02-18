# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if linklist is empty
        if head == None:
            return None
        #if linklist has one node
        if head.next == None:
            return head
        
        odd = head
        even = head.next
        evenHead = head.next
        
        #when even goes to the end or out of range
        while even and even.next:
            #make odd and even connect two positons
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        #connect the odd elements to even elements
        odd.next = evenHead
        
        return head