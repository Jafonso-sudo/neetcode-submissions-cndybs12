# Solution: O(n) time & space
# - keep a stack of the open parenthesis
# - when we find a new open parenthesis we push it to the stack
# - when we find a close parenthesis we check if the top matches, if not return false, else pop it
# - at the end we check if our stack is empty and return that

# BUGS
# - Early termination had an AND instead of an OR initially

class Solution:
    # def check_match(self, o, c):
    #     return f"{o}{c}" in "(){}[]"

    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     for c in s:
    #         if c in "({[":
    #             stack.append(c)
    #         elif not stack or not self.check_match(stack[-1], c):
    #             return False
    #         else:
    #             stack.pop()
        
    #     return len(stack) == 0

    def isValid(self, s: str) -> bool:
        stack = []
        match = {"{":"}", "(":")", "[":"]"}
        for c in s:
            if c in match:
                stack.append(c)
            elif stack and c == match[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0