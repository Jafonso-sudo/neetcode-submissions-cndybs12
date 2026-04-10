# Solution
# - The stack part is trivial
# - The minstack thing relies on identifying that e.g.
#   [0, 1, 2] <- top means that we only need to store 0 since all numbers above it are larger
#   [2, 1, 0] <- top means we have to store all
#   Generalizing: We need to store the numbers that appear in decreasing order
#   When we get a push we check:
#   - Is this number smaller or equal than the top of the min stack? if so add to it, else ignore
#   When we get a pop we check:
#   - Is this number on the minstack, then pop it out from there

# Single Stack Solution
# - Spoiled: We store the difference to the previous seen minimum
# Example: [2, 0, -2, 0]
# Push 2
# [0] min=2
# Push 0
# [0, -2] min=0
# Push -2
# [0, -2, -2] min=-2
# Push 0
# [0, -2, -2, 2] min=-2
# Pop 0
# [0, -2, -2] min=-2 -> 2 + (-2) = 0
# Pop -2
# [0, -2] min=0 -> -2 + 0 = -2
# Notice -2 < 0, so min must be updated
# new_min = old_min - (-2) = -2 + 2 = 0
# -> -2 + 0 = -2
# Pop 0
# [0] min= 0 - (-2) = 2 -> -2 + 2 = 0
# Pop 2
# [] min=inf (since empty) -> 0 + 2 = 2


# Bugs
# - Initially was calling getMin without checking if stack was empty 

# Notes
# - Didn't come up with the single stack approach initially, it is interesting (but bit hacky)

# class MinStack:
#     # 2-Stack Approach
#     def __init__(self):
#         self.stack: list = []
#         self.min_stack: list = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.min_stack or self.getMin() >= val:
#             self.min_stack.append(val)

#     def pop(self) -> None:
#         val = self.stack.pop()
#         if val == self.getMin():
#             self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]

class MinStack:
    # Single-Stack Approach
    def __init__(self):
        self.stack: list = []
        self.min_val = -1

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.min_val -= val

    def top(self) -> int:
        val = self.stack[-1]
        if val >= 0:
            return val + self.min_val
        else:
            return self.min_val

    def getMin(self) -> int:
        return self.min_val
