# Solution: O(n * l)
# - Combine strings separated by a non ASCII character
# - Time/space is gonna be the total length of the strings combined

# Assuming any possible set of characters:
# - We need to escape any divider character
# - We also need to escape the escape character (iteratively)
# ["a", "b", ",", "\,", "\\", "c"]
# ["a,b,\,,\\\,,\\\\,c"]
# Search for odd number of \ followed by , and split on last \,
# Replace (\\)^b with (\)^b
# TODO: Don't know how to actually do this cleanly/efficiently in code?

# Saw Solution: Much simpler, just encode "neet" -> "4#neet"

# Cheatsheet
# - 'a' -> 97 w/ ord('a') AND 97 -> 'a' w/ chr(97)

# Bug
# - Initially, failed to distinguish [""] from []

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         return chr(257) + chr(257).join(strs) + chr(257)

#     def decode(self, s: str) -> List[str]:
#         if not s:
#             return []
#         return s.split(chr(257))[1:-1]

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + '#')
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            sep_idx = i + s[i:].find('#')
            s_len = int(s[i:sep_idx])
            s_start = sep_idx + 1
            s_end = s_start + s_len
            sub_s = s[s_start : s_end]
            i = s_end
            result.append(sub_s)

        return result
