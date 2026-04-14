# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Cheatsheet
# - Slow & fast pointer strategy can be used to find the middle of the array in a more efficient way too

# Solution
# - First do a run to get the size of the array
# - Add all the first n/2 elements, while connecting the other two

# https://gemini.google.com/app/f4bd9e5896e56c82

class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     n = 0
    #     cur = head
    #     while cur:
    #         n += 1
    #         cur = cur.next
        
    #     # Get tail
    #     tail = head
    #     for i in range((n + -1) // 2):
    #         tail = tail.next
    #     temp = tail
    #     tail = tail.next
    #     temp.next = None

    #     # Reverse tail
    #     rev_tail = None
    #     while tail:
    #         temp = tail.next
    #         tail.next = rev_tail
    #         rev_tail = tail
    #         tail = temp

    #     # Interleave head and tail
    #     cur = head
    #     while rev_tail:
    #         temp = cur.next
    #         temp_tail = rev_tail.next
    #         cur.next = rev_tail
    #         rev_tail.next = temp
    #         rev_tail = temp_tail
    #         cur = temp

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        rev_tail = slow.next = None # sever link between head and tail
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