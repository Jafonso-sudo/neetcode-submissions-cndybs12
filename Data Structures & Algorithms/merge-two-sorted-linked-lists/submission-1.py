# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Notes
# - I didn't do the obvious efficiency hack: when one is done, use the other as the tail

class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     head = tail = None
         

    #     while list1 or list2:
    #         if list1 and (not list2 or list1.val <= list2.val):
    #             next = list1
    #             list1 = list1.next
    #         else:
    #             next = list2
    #             list2 = list2.next
    #         if not head:
    #             head = next
    #             tail = next
    #         else:
    #             tail.next = next
    #             tail = tail.next
        
    #     return head
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        
        return head.next
        