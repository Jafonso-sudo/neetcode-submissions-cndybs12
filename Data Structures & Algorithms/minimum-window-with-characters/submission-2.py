# BUGS I HAD
# - FOUND BEFORE RUNNING: not doing r - l + 1 (just doing r - l)
# - Not checking if s[l] was in count
# - Not checking for out of bounds for l

# https://gemini.google.com/app/7f8dc19d6103321d

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = {}
        matches_left = 0
        for c in t:
            if c not in count:
                matches_left += 1
                count[c] = 0
            count[c] += 1

        l = 0
        res_l, res_r = -1, len(s)
        for r in range(len(s)):
            # Consider added character
            c = s[r]
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    matches_left -= 1
            
            # Now try to get rid of characters on the left
            while l < r and (s[l] not in count or count[s[l]] < 0):
                if s[l] in count:
                    count[s[l]] += 1
                l += 1

            # Check for condition
            if matches_left == 0 and res_r - res_l > r - l + 1:
                res_r, res_l = r + 1, l
        
        return "" if res_l == -1 else s[res_l:res_r]

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = {}
        matches_left = 0
        for c in t:
            if c not in count:
                matches_left += 1
                count[c] = 0
            count[c] += 1

        l = 0
        res_l, res_r = -1, len(s)
        for r in range(len(s)):
            # Consider added character
            c = s[r]
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    matches_left -= 1
            
            # Now try to get rid of characters on the left
            while l < r and (s[l] not in count or count[s[l]] < 0):
                if s[l] in count:
                    count[s[l]] += 1
                l += 1

            # Check for condition
            if matches_left == 0 and res_r - res_l > r - l + 1:
                res_r, res_l = r + 1, l
        
        return "" if res_l == -1 else s[res_l:res_r]
