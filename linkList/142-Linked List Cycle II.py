# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        #fast and slow pointer, run until the meet or fast goes to the end
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            #if they meet, break
            if fast == slow:
                break
        #check if it is a loop or not
        if fast == None or fast.next == None:
            return None
        #let fast or slow pointer to the head again
        fast = head
        #run until they meet, return the pointer which they meet
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast