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
# - To find first occurrence of a substring in a string use str.find(sub_str)
# - IMPORTANT: s[i] creates a copy, therefore my original decode was O(n^2)
#   To avoid things like this, when we don't actually want the substring directly, use optional params e.g. str.find(sub[, start[, end]])

# Bug
# - Initially, failed to distinguish [""] from []
# - Initially, had num + str instead of str(num) + str

# https://gemini.google.com/app/8c145eed0d860b78

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

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            sep_idx = s.find("#", i)
            length = int(s[i:sep_idx])
            s_start = sep_idx + 1
            s_end = s_start + length
            result.append(s[s_start : s_end])
            i = s_end

        return result

# For the escaping option
# from typing import List

# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         if strs is None:
#             return ""
            
#         encoded_parts = []
#         for s in strs:
#             # 1. Escape the escape character first!
#             # (If we did the comma first, we'd double-escape the backslash we just added)
#             s = s.replace('\\', '\\\\')
            
#             # 2. Escape the delimiter
#             s = s.replace(',', '\\,')
            
#             # 3. Add the unescaped delimiter to mark the end of the string
#             encoded_parts.append(s + ',')
            
#         return "".join(encoded_parts)

#     def decode(self, s: str) -> List[str]:
#         # Handle the genuinely empty array edge case
#         if not s: 
#             return []
            
#         result = []
#         current_string = []
#         i = 0
        
#         while i < len(s):
#             if s[i] == '\\':
#                 # State: Escape. 
#                 # Blindly grab the next character as literal data and jump 2 spaces.
#                 current_string.append(s[i + 1])
#                 i += 2
#             elif s[i] == ',':
#                 # State: Terminator. 
#                 # We reached the end of a string. Save it and reset the buffer.
#                 result.append("".join(current_string))
#                 current_string = []
#                 i += 1
#             else:
#                 # State: Normal character.
#                 # Just add it to the buffer and move forward.
#                 current_string.append(s[i])
#                 i += 1
                
#         return result