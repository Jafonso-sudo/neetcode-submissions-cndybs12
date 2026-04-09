# Solution 1: Time/Space O(n)
# - Traverse left to right once and right to left once keep track of the product

# Solution 2: Time O(n), Space O(1) uses division
# - Use two pointer and traverse left to right
# CORRECTION: Even easier, just calculate total product once, then another pass divides...

# Solution 3: Time O(n), Space O(1) does not use division
# - Traverse once from left computing left side
# - Traverse once from right computing right side

# Bug
# - In inverse range, I had range(len(nums) - 1, 0) --- without the -1 increment, I thought python would change the default but no

# Cheatsheet
# - Range: range([start,] stop[, increment=1]) --- need to explicitely change increment to negative if start > stop!

# https://gemini.google.com/app/55110eb13ad0cc17

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

# GEMINI POLISH
# - Better variable names
# - Avoid the (+1)/(-1) indexing. I agree it's cleaner.

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         result = [1] * n
        
#         # Pass 1: Calculate prefixes
#         # result[i] contains the product of all elements to the LEFT of i
#         for i in range(1, n):
#             result[i] = result[i - 1] * nums[i - 1]
            
#         # Pass 2: Calculate suffixes and multiply on the fly
#         # suffix_product holds the product of all elements to the RIGHT of i
#         suffix_product = 1
#         for i in range(n - 1, -1, -1):
#             # Multiply the prefix by the suffix
#             result[i] *= suffix_product
#             # Update the suffix product for the next iteration
#             suffix_product *= nums[i]
            
#         return result