# Discussion with interviewer:

# Solution: O(n) time, O(1) space
# - Keep two pointers (one from the left and one from the right)
# - First pointers find the next alphanumeric character
# - Then we check if they are on the same character (when set to lower case)
# - Stop when pointers pass eachother

# I would ask for whether he knows what built-in function I could alphanumeric, explain I would use ord(.) to do it manually otherwise.

# Self-Notes

# Cheatsheet
# - str.isalnum() checks if it's alphanumeric string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = -1, len(s)

        while l < r:
            while True:
                l += 1
                if l >= r:
                    return True
                if s[l].isalnum():
                    break
            while True:
                r -= 1
                if s[r].isalnum():
                    break

            if s[l].lower() != s[r].lower():
                return False
        
        return True
        