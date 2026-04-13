# Notes
# - This exercise just drained me. I didn't feel like working on it. It's not particularly hard, but it's so annoying thinking of the division of cases you have to consider...

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # If they're in different "quadrants" move towards right quadrant
            if target <= nums[-1] <= nums[0] and nums[m] >= nums[0]:
                l = m + 1
            elif nums[m] <= nums[-1] <= nums[0] and target >= nums[0]:
                r = m
            # If they're in the same quadrant
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        
        return -1