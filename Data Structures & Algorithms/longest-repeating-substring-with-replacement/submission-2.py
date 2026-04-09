# Solution: Sliding Window O(n) Time, O(1) Space O("# of letters")
# - Start two pointers overlapping, iterate over r
# - Keep track of counter of letters in our window, and which is the most common
# - If the number of non-common letters is < k, we move the left pointer to the right


class Solution:
    def _get_used_replacements(self, counter: dict) -> int:
        l = 0
        most_common = 0
        for v in counter.values():
            l += v
            most_common = max(most_common, v)
        
        return l - most_common

    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l, r = 0, 0
        result = 0
        for r, c in enumerate(s):
            counter[c] += 1
            
            while (used := self._get_used_replacements(counter)) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    counter.pop(s[l])
                l += 1
            
            result = max(result, r - l + 1)
        
        return result
            