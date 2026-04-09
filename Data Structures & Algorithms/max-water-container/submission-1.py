# Solution 1: Brute-Force O(n^2)
# - Double loop, find the max

# Solution 2: Sliding Window O(n)
# - Keep a left and right pointer
# - Move the pointer of the smallest

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            result = max(result, width * height)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return result
