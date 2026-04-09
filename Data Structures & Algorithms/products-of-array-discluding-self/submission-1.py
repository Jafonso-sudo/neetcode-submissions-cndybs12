# Solution 1: Time/Space O(n)
# - Traverse left to right once and right to left once keep track of the product

# Solution 2: Time O(n), Space O(1) uses division
# - Use two pointer and traverse left to right

# Solution 3: Time O(n), Space O(1) does not use division
# - Traverse once from left computing left side
# - Traverse once from right computing right side

# Bug
# - In inverse range, I had range(len(nums) - 1, 0) --- without the -1 increment, I thought python would change the default but no

# Cheatsheet
# - Range: range([start,] stop[, increment=1]) --- need to explicitely change increment to negative if start > stop!

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Left -> Right
        for i in range(len(nums) - 1):
            res[i + 1] = res[i] * nums[i]

        # Right -> Left
        cur = 1
        for i in range(len(nums) - 1, 0, -1):
            cur *= nums[i]
            res[i - 1] *= cur

        return res
