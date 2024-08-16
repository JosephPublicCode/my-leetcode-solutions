# leetcode 206

# Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        prev, cur = None, head

        while cur: 
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
# Time Complexeity: O(n)
# Space Complexeity: O(1)

# recursive approach

class Solution:
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        if not head: 
            return None
        
        next_head = head
        if head.next: 
            next_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return next_head
    
