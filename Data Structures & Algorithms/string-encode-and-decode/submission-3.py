# Solution: O(n * l)
# - Combine strings separated by a non ASCII character
# - Time/space is gonna be the total length of the strings combined

# Assuming any possible set of characters:
# - We need to escape any divider character
# - We also need to escape the escape character (iteratively)

# Cheatsheet
# - 'a' -> 97 w/ ord('a') AND 97 -> 'a' w/ chr(97)


# Bug
# - Initially, failed to distinguish [""] from []

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return chr(257) + chr(257).join(strs) + chr(257)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s.split(chr(257))[1:-1]
