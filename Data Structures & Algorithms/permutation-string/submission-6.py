# Solution: O(n) sliding window
# - Get a counter for the letters in s1
# - Iterate over r in s2
# - Move l to r when we find a letter than does not belong <-- WRONG: move only one step at a time, don't be an eager beaver
# - Later if we want to optimize we can store when a letter was first seen <-- PROBLEM: How to do this in O(1) space?
# - Key: Consider only the windows of possible sizes (DID NOT FIGURE THIS OUT BY MYSELF)

class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     counter = defaultdict(int)
    #     for c in s1:
    #         counter[c] += 1
        
    #     l = 0
    #     for r, c in enumerate(s2):
    #         counter[c] -= 1
    #         while counter[c] < 0:
    #             counter[s2[l]] += 1
    #             l += 1

    #         if r - l + 1 == len(s1):
    #             return True

    #     return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        ca = ord('a')

        # Build initial window
        counter = [0] * 26
        for i in range(len(s1)):
            counter[ord(s1[i]) - ca] += 1
            counter[ord(s2[i]) - ca] -= 1
        matches = 0
        for i in range(26):
            matches += counter[i] == 0
        if matches == 26:
                return True

        # Iterate on windows
        for r in range(len(s1), len(s2)):
            # Update r
            cr = ord(s2[r]) - ca
            if counter[cr] == 0:
                matches -= 1
            counter[cr] -= 1
            if counter[cr] == 0:
                matches += 1

            # Update l
            cl = ord(s2[r - len(s1)]) - ca
            if counter[cl] == 0:
                matches -= 1
            counter[cl] += 1
            if counter[cl] == 0:
                matches += 1
            
            if matches == 26:
                return True
        
        return False


