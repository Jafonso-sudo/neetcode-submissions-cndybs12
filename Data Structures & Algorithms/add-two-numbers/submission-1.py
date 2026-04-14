# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Bugs
# - Was initially not keeping track of tail and always replacing res 
# - Initially had carry = cur > 10 instead of cur >= 10

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        tail = res
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            cur = val1 + val2 + carry
            carry = int(cur >= 10)
            cur -= carry * 10
            tail.next = ListNode(cur)
            tail = tail.next
        if carry:
            tail.next = ListNode(1)
        
        return res.next
        