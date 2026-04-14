# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Notes
# - Was confused what they meant with O(1) space, I get they meant in-place even though they didn't say that

class Solution:
    # "O(1) Space"
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     tail = None
    #     while head:
    #         tail = ListNode(head.val, tail)
    #         head = head.next
    #     return tail

    # O(1) Space
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        
        return tail