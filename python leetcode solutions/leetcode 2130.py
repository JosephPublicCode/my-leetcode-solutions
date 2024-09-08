# leetcode 2130 

# Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next: 
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        max_val = 0
        while prev: 
            max_val = max(max_val, prev.val + slow.val)
            slow, prev = slow.next, prev.next
        return max_val
            
# O(n) Time Complexeity
# O(1) Space Complexeity

'''
Method: 
iterative reversal of the first half of the linked list. the inside out appraoch is easier to code that the outside in approach. 
1. Iterate until the fast pointer reaches the end of the list meaning that the slow pointer is half way. 
2. iterate through the reversed and non reversed portion checking for the max
'''



        
