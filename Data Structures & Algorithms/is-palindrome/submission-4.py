# Discussion with interviewer:

# Solution: O(n) time, O(1) space
# - Keep two pointers (one from the left and one from the right)
# - First pointers find the next alphanumeric character
# - Then we check if they are on the same character (when set to lower case)
# - Stop when pointers pass eachother

# (I could also solve it with a queue, but that would be O(n) space and the same time complexity)
# (For the cleanest code, but in O(n) space, could also just filter the characters first, then check if the reverse matches it)

# I would ask for whether he knows what built-in function I could alphanumeric, explain I would use ord(.) to do it manually otherwise.

# Self-Notes

# Cheatsheet
# - str.isalnum() checks if it's alphanumeric string

# Bugs
# - I was first checking s[l] instead of l >= r, causing an out of index exception.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = -1, len(s)

#         while l < r:
#             while True:
#                 l += 1
#                 if l >= r:
#                     return True
#                 if s[l].isalnum():
#                     break
#             while True:
#                 r -= 1
#                 if s[r].isalnum():
#                     break

#             if s[l].lower() != s[r].lower():
#                 return False
        
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True

        
        