# Option 1: O(n log n) Time, O(n) Space
# - Sort the numbers (while keeping track of original indexes)
# - Do a two pointer approach, if the sum of them is too large, move right pointer, else left

# Option 2: O(n^2) Time, O(1) Space
# - Double for loop, find the match

# Option 3: O(n) Time, O(n) Space <-- Best solution
# - Keep a hashmap of the existing numbers, check if there's a match

# Problem
# - I almost started on Option 1 before realizing this is obviously Option 3

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen_numbers = dict()

#         for i, num in enumerate(nums):
#             match = target - num
#             if match in seen_numbers:
#                 return [seen_numbers[match], i]
#             else:
#                 seen_numbers[num] = i
        
#         return []

# Post Review
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {} # slightly faster

        for i, num in enumerate(nums):
            match = target - num
            if match in seen_numbers:
                return [seen_numbers[match], i]
            seen_numbers[num] = i

