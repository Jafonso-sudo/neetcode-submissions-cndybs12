# Solution: O(n log n) time, O(n) space
# - Sort the cars by position
# - Calculate how many timesteps they would take to arrive based on their speed
# - Push the farthest car on stack
# - If next car would reach before or at same time, we skip it. Else we add to the stack.

# Bugs
# - Forgot tuples are immutable initially was storing data as tuples
# - Forgot to distinguish between arriving at the exact same time, and every so slightly after/before
#    (Was unecessarily truncating float arrival to int)

# Cheatsheet
# - list.sort(reverse=True/False, key=lambda x: x)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        data = []

        # Check how fast we arrive
        for i in range(n):
            arrival = (target - position[i]) / speed[i]
            data.append([position[i], arrival])
        data.sort(key=lambda x: -x[0])

        res = 1
        for i in range(1, n):
            # Check if we catchup
            if data[i - 1][1] >= data[i][1]:
                data[i][1] = data[i-1][1]
                continue
            res += 1
        return res