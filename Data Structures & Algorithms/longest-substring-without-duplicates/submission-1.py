class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     present = set()
    #     result = l = 0
    #     for r, c in enumerate(s):
    #         while c in present:
    #             present.remove(s[l])
    #             l += 1
    #         present.add(c)
    #         result = max(result, len(present))
        
    #     return result

    # Improvement: Avoids the inner while loop by tracking the index of the seen character
    def lengthOfLongestSubstring(self, s: str) -> int:
            present = {}
            result = l = 0
            for r, c in enumerate(s):
                if c in present:
                    l = max(l, present[c] + 1)
                present[c] = r
                result = max(result, r - l + 1)
            
            return result