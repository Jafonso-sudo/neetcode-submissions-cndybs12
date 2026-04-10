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

# Bugs
# - Initially was calling getMin without checking if stack was empty 

class MinStack:

    def __init__(self):
        self.stack: list = []
        self.min_stack: list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.getMin() >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
