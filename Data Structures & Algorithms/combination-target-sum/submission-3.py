# Solution:
# - Sort numbers, and brute force combine them

# Bugs
# - Initially did not have the case where we don't add any number (the final comb(i + 1) call)
# - Initially forgot to decrement cur_sum after popping item
# - Inefficiency: Originally didn't have check to see if it was even worth proceeding to the next number

# Gemini Review
# - We only need nonlocal for reassigning immutable variables, here we only would need it for cur_sum
# - By passing cur_sum and current directly, it's easier to reverse the additions
# - I personally prefer my approach, but it iterates through solutions the same way as in the solution

# https://gemini.google.com/app/01b1897a136acede

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []
        current = []
        cur_sum = 0
        nums.sort()
        n = len(nums)

        def comb(i: int):
            nonlocal cur_sum # solutions, current, cur_sum, nums, n
            if cur_sum == target:
                solutions.append(current.copy())
                return
            if i == n:
                return
            
            num = nums[i]
            max_cur = (target - cur_sum) // num
            # Include number
            for _ in range(max_cur):
                current.append(num)
                cur_sum += num
                comb(i + 1)
            for _ in range(max_cur):
                current.pop()
                cur_sum -= num
            # Skip number
            if i < n - 1 and nums[i + 1] <= target - cur_sum:
                comb(i + 1)
        comb(0)

        return solutions