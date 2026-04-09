# Solution: O(n) sliding window
# - Get a counter for the letters in s1
# - Iterate over r in s2
# - Move l to r when we find a letter than does not belong <-- WRONG: move only one step at a time, don't be an eager beaver
# - Later if we want to optimize we can store when a letter was first seen <-- PROBLEM: How to do this in O(1) space?

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for c in s1:
            counter[c] += 1
        
        l = 0
        for r, c in enumerate(s2):
            counter[c] -= 1
            while counter[c] < 0:
                counter[s2[l]] += 1
                l += 1

            if r - l + 1 == len(s1):
                return True

        return False