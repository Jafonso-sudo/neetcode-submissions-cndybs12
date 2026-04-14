# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None
         

        while list1 or list2:
            if list1 and (not list2 or list1.val <= list2.val):
                next = list1
                list1 = list1.next
            else:
                next = list2
                list2 = list2.next
            if not head:
                head = next
                tail = next
            else:
                tail.next = next
                tail = tail.next
        
        return head
        