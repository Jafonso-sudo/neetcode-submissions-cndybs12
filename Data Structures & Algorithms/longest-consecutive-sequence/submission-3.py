# INTERESTING

# Solution:
# - Traverse creating several linked list-like structures
# - At the end we iterate through those linked list-like structures and see 
# - Key: Keep track of which are the first elements in the sequence

# Notes
# - I think I took way too much time in this exercise, I'm a bit tired but still feel a lil dumb
# - I also forgot to discuss trade-offs: sorting in n log n, but with O(1) time; alternative of using union-find but with more boilerplate

# https://gemini.google.com/app/f32f612283a983a6

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         has_prev = set()
#         seen = set()
#         for num in nums:
#             seen.add(num)
#             has_prev.add(num + 1)
        
#         result = 0
#         for num in nums:
#             if num in has_prev:
#                 continue
#             seq_len = 1
#             while num + 1 in seen:
#                 seq_len += 1
#                 num += 1
#             result = max(result, seq_len)

#         return result

# Cleaner
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        
        res = 0
        for num in nums:
            if num - 1 in nums:
                continue

            seq_len = 1
            while num + seq_len in nums:
                seq_len += 1

            res = max(res, seq_len)
        
        return res

# Gemini
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         if not nums:
#             return 0
            
#         num_set = set(nums)
#         longest_streak = 0
        
#         for num in num_set:
#             # Only start counting if this is the FIRST number in a sequence
#             if num - 1 not in num_set:
#                 current_num = num
#                 current_streak = 1
                
#                 # Keep walking up the sequence
#                 while current_num + 1 in num_set:
#                     current_num += 1
#                     current_streak += 1
                    
#                 longest_streak = max(longest_streak, current_streak)
                
#         return longest_streak 
