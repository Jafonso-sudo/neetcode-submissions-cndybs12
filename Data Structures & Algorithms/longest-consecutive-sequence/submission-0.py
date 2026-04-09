# Solution:
# - Traverse creating several linked list-like structures
# - At the end we iterate through those linked list-like structures and see 
# - Key: Keep track of which are the first elements in the sequence

# Notes
# - I think I took way too much time in this exercise, I'm a bit tired but still feel a lil dumb

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        has_prev = set()
        seen = set()
        for num in nums:
            seen.add(num)
            has_prev.add(num + 1)
        
        result = 0
        for num in nums:
            if num in has_prev:
                continue
            seq_len = 1
            while num + 1 in seen:
                seq_len += 1
                num += 1
            result = max(result, seq_len)

        return result