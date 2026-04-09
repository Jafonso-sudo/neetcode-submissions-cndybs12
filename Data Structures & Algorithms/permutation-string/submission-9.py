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

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s2) < len(s1):
    #         return False
    #     ca = ord('a')

    #     # Build initial window
    #     counter = [0] * 26
    #     for i in range(len(s1)):
    #         counter[ord(s1[i]) - ca] += 1
    #         counter[ord(s2[i]) - ca] -= 1
    #     matches = 0
    #     for i in range(26):
    #         matches += counter[i] == 0

    #     # Iterate on windows
    #     for r in range(len(s1), len(s2)):
    #         if matches == 26:
    #             return True

    #         # Update r
    #         cr = ord(s2[r]) - ca
    #         if counter[cr] == 0:
    #             matches -= 1
    #         counter[cr] -= 1
    #         if counter[cr] == 0:
    #             matches += 1

    #         # Update l
    #         cl = ord(s2[r - len(s1)]) - ca
    #         if counter[cl] == 0:
    #             matches -= 1
    #         counter[cl] += 1
    #         if counter[cl] == 0:
    #             matches += 1
        
    #     return matches == 26

    # GEMINI SLOP
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Use two arrays of size 26 for O(1) space
        s1_counts = [0] * 26
        window_counts = [0] * 26
        
        # Populate the target frequencies
        for char in s1:
            s1_counts[ord(char) - ord('a')] += 1
            
        left = 0
        for right, char in enumerate(s2):
            char_idx = ord(char) - ord('a')
            window_counts[char_idx] += 1
            
            # If our window is larger than s1, shrink it from the left
            if right - left + 1 > len(s1):
                left_char_idx = ord(s2[left]) - ord('a')
                window_counts[left_char_idx] -= 1
                left += 1
                
            # Python's list comparison is executed in C and is extremely fast
            if window_counts == s1_counts:
                return True
                
        return False


