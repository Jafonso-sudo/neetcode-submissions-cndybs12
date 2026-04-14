# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast:
            if fast.next == slow:
                return True
            fast = fast.next
            if not fast:
                return False
            elif fast.next == slow:
                return True
            fast = fast.next
            slow = slow.next
        
        return False