# Solution: DP O(n) time O(1) space
# - robbed[i]: maximum number of money robbed until house i
# - robbed[0] = nums[0]
# - robbed[1] = max(nums[0], nums[1])
# - robbed[i] = max(robbed[i - 1], robbed[i - 2] + nums[i])

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for money in nums:
            res = max(cur, prev + money)
            prev, cur = cur, res
        return cur
        