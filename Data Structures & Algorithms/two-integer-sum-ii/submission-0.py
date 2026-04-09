# Solution:
# - Sliding pointers
# - Left pointer moves if we're below the target
# - Right poiter moves if we're above the target
# - At the end check if we hit the target (or in this case since there is exactly one valid solution, we don't need the check)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r  = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum < target:
                l += 1
            elif cur_sum == target:
                return [l + 1, r + 1]
            else:
                r -= 1

        return [l + 1, r + 1]