class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        present = set()
        result = l = r = 0
        for r, c in enumerate(s):
            while c in present:
                present.remove(s[l])
                l += 1
            present.add(c)
            result = max(result, len(present))
        
        return result
            