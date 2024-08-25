# leetcode 328

# Odd Even Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: 
            return
        l,r = head, head.next
        
        while r and r.next: 
            r_node = ListNode(r.next.val)

            tmp = l.next
            r_node.next = tmp
            l.next = r_node
            r.next = r.next.next


            l = l.next
            r = r.next
        return head