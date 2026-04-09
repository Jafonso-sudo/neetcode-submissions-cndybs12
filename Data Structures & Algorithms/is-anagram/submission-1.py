# Option 1: O(1) Space
# - Sort the array first O(n log n)
# - Iterate through the arrays comparing values O(n)

# Option 2: O(n) Time, O(n) Space
# - Iterate through the first string counting the letters in a hash map O(n) time and space
#   Better for long arrays: Initialize array of zeroes of length int(z) - int(a) and count there

# Cheatsheet
# - Turn char into int using ord(char)

# Bug
# - Initially had not subtracted ord('a') from ord(char)
# - Initially had ord('z') - ord('a') without the + 1

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

