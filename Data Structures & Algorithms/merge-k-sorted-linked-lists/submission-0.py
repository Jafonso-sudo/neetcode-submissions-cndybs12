# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution
# - Keep heap of size k (the head of the lists), keep popping smallest

# Cheatsheet
# - Heap: heapq.heapify(list) turns normal list into min-heap: heapq.heappush(heap, item)/heappop(heap) are the base.
# - heapq.heappoppush(heap, item) -> push new item then pop smallest, heapq.heapreplace(heap, item) -> pop smalles then push | faster than individual 
# - All these have maxheap variants by appending _max to the function name
#   https://docs.python.org/3/library/heapq.html

# Bugs
# - Forgot to set the new tail
# - Did not realize heapify was in-place

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tail = ListNode()
        heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        while heap:
            val, i = heapq.heappop(heap)
            tail.next = lists[i]
            lists[i] = lists[i].next
            tail = tail.next
            tail.next = None
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return head.next