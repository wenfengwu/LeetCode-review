# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        #while two pointers has not intersection
        while p1 != p2:
            #if p1 reach the end, move it to headB
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            #if p2 reach the end, move it to headA
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1
