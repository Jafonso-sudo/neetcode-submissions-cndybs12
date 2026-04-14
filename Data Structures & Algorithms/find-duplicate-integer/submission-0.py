# Note
# - This is a HARD exercise that requires knowledge of a specific algorithm to detect the first node of a cycle
# - Floyd's Algorithm: Begin a slow and fast pointer. Find the first point they intersect and stop. Begin a second slow pointer and stop where both slow pointers intersect. That is the first element of the cycle.
# - This requires interpreting this list of nums as a graph (or LinkedList with a cycle), where the num is the index the node points to.
# - This works because cycles will begin with the duplicate number and we have a guarantee that there's at least one node (0) which does not belong to the cycle.
# - I DID NOT FIGURE THIS OUT BY MYSELF AT ALL, GOT STUCK AND LOOKED AT THE SOLUTIONS

# Bug initially had while fast != slow which obviously wouldn't run at all given you initialize both to 0

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        
        return start