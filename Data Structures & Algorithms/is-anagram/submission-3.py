# Option 1: O(n) Time, O(1) Space
# - Iterate through the first string counting the letters in a hash map O(n) time and space
#   Better for long arrays: Initialize array of zeroes of length int(z) - int(a) and count there

# Cheatsheet
# - Turn char into int using ord(char)
# - Note: Python sort() --- Timsort --- uses O(n) space, but in-place is possible with O(1)
# - In interviews, trust the constraints (don't code safeguards for impossible inputs)
#  (However, do verbalize it)
# - This could also be solved with just Counter(s) == Counter(t)

# Bug
# - Initially had not subtracted ord('a') from ord(char)
# - Initially had ord('z') - ord('a') without the + 1
# - Initially I said this solution is O(n) space, but it's O(1) -- fixed size

# FEEDBACK: https://gemini.google.com/app/d8ea1f64dbd1d329

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * (ord('z') - ord('a') + 1)
        base_idx = ord('a')
        for char in s:
            counter[ord(char) - base_idx] += 1
        
        for char in t:
            char_idx = ord(char) - base_idx
            if counter[char_idx] > 0:
                counter[char_idx] -= 1
            else:
                return False
        
        return True

