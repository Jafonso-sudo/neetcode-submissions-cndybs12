class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        # Solution w/ first house included
        prev_first, cur_first = 0, nums[0]
        # Solution w/out first house included
        prev = cur = 0
        for i in range(1, len(nums)):
            prev_first, cur_first = cur_first, max(cur_first, prev_first + nums[i])
            prev, cur = cur, max(cur, prev + nums[i])
        
        return max(cur, prev_first)
