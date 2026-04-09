# Had initially not realized we could use a deque for it and gemini gave a bit of a too strong of a tip during the mock interview

# https://gemini.google.com/app/6d55281d7a12bbba

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums) - k + 1)

        largest_decreasing = deque()
        for r in range(len(nums)):
            # Get rid of anything smaller than the new number we're seeing now
            while largest_decreasing and nums[largest_decreasing[-1]] < nums[r]:
                largest_decreasing.pop()
            largest_decreasing.append(r)

            if r + 1 < k:
                continue
            # Check if we need to get rid of our largest
            if largest_decreasing[0] <= r - k:
                largest_decreasing.popleft()

            result[r - k + 1] =  nums[largest_decreasing[0]]

        return result