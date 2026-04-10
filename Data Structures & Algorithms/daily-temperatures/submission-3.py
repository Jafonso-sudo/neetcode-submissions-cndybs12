# [30,38,30,36,35,40,28]

# [30,38,30,36,35,40]
# Res: [..., 0]
# 28 (-1)

# [30,38,30,36,35]
# We look in the stack and pop until we find a warmer temp, we don't
# Res: [..., 0, 0]
# 40 (-2)

# [30,38,30,36]
# We look in the stack and find a warmer temp
# Res: [..., 1, 0, 0]
# 35 (-3), 40 (-2)

# Cheatsheet
# - list.reverse() to in-place reverse array, list[::-1] to create new, reversed(list) for iterator
# - Interesting: The DP approach that relies on total # of hops being O(n) is cool

# Bugs
# - Had forgotten to append to stack at the end
# - Was popping the top of the stack instead of just looking at it when updating res

class Solution:
    # O(n) extra space (besides O(n) output space)
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = [0] * len(temperatures)
    #     stack = []
    #     for i in range(len(temperatures) - 1, -1, -1):
    #         t = temperatures[i]
    #         while stack and stack[-1][1] <= t:
    #             stack.pop()
    #         res[i] = stack[-1][0] - i if stack else 0
    #         stack.append((i, t))
        
    #     return res

    # O(1) extra space
    # Bugs: Initially had forgotten to do a check for res[j] at calc res[i]
    # - Wasn't checking properly for res[j] = 0 implications
    # - Also had temp[j] < temp[i] instead of <=
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while temperatures[j] <= temperatures[i]:
                if not res[j]:
                    j = n
                    break
                j += res[j]
            if j < n:
                res[i] = j - i
        return res
