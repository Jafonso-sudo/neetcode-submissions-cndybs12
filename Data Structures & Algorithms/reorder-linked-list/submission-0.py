# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution
# - First do a run to get the size of the array
# - Add all the first n/2 elements, while connecting the other two

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        # Get tail
        tail = head
        for i in range((n + -1) // 2):
            tail = tail.next
        temp = tail
        tail = tail.next
        temp.next = None

        # Reverse tail
        rev_tail = None
        while tail:
            temp = tail.next
            tail.next = rev_tail
            rev_tail = tail
            tail = temp

        # Interleave head and tail
        cur = head
        while rev_tail:
            temp = cur.next
            temp_tail = rev_tail.next
            cur.next = rev_tail
            rev_tail.next = temp
            rev_tail = temp_tail
            cur = temp