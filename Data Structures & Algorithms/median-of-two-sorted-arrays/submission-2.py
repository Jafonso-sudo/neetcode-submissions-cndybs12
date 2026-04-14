# Cheatsheet
# - Was doing n + m % 2 instead of (n + m) % 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        n, m = len(small), len(big)
        half = (n + m + 1) // 2

        l, r = 0, n
        while l <= r:
            s = (l + r) // 2
            s_el = None if s == 0 else small[s - 1]
            s_next = None if s >= n else small[s]

            b = half - s
            b_el = None if half - s <= 0 else big[b - 1]
            b_next = None if b >= m else big[b]

            if s_next is not None and b_el is not None and s_next < b_el:
                l = s + 1
            elif b_next is not None and s_el is not None and b_next < s_el:
                r = s - 1
            else:
                res = s_el if s_el is not None and (b_el is None or s_el > b_el) else b_el
                if (n + m) % 2 == 0:
                    compl = s_next if s_next is not None and (b_next is None or s_next < b_next) else b_next
                    res = (res + compl) / 2
                return res

        return -1
