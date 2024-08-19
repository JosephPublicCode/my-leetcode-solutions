# leetcode 2095

# Delete the middle node of a linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if head.next == None: 
            return head.next
        start, dummy = head, ListNode(0,head)
        s, f = dummy, start
        while f: 
            if f.next == None:
                s.next = s.next.next
                return start
            if f.next and f.next.next == None: 
                s = s.next 
                s.next = s.next.next
                return start
            f = f.next.next
            s = s.next
        return start