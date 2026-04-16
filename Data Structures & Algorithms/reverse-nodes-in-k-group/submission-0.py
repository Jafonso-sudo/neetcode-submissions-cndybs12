# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution: O(n) time, O(1) space
# - Just do the reverse trick multiple times

# Bug
# - I always forget to keep the head & tail of the result
# - Wasn't updating cur
# - Didn't read the part of "if there's less than k remaining" etc etc (don't have patience to do something better, so will just get n first)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head
        result = tail = ListNode()
        n = 0
        count_head = head
        while count_head:
            n += 1
            count_head = count_head.next
        while head:
            cur = None
            new_tail = head
            if n < k:
                tail.next = head
                break
            for _ in range(k):
                temp_next = head.next
                head.next = cur
                cur = head
                head = temp_next
            n -= k
            tail.next = cur
            tail = new_tail
                
        return result.next
