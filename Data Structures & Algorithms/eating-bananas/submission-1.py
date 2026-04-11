# Solution: n log m
# - Do binary search over the solution k O(log m) - m = max in array
# - Each time see if it works in O(n) time

# Bug
# - Initially had a division by 0 cause I was starting l from 0 dum dum

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            k = (l + r) // 2
            used_hours = 0
            for pile in piles:
                used_hours += math.ceil(pile / k)
            if used_hours > h:
                l = k + 1
            else:
                r = k

        return l
