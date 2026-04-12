# Bug
# - Initially had an out of bounds exception when accessing nums[m+1] (example input: [2,1])
#    Solved by initializing r to len(nums) -1 (instead of len(nums) -- that case being explicitely checked above anyways)

class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     leftmost, rightmost = nums[0], nums[-1]
    #     if leftmost <= rightmost:
    #         return leftmost

    #     l, r = 0, len(nums) - 1
    #     while l < r:
    #         m = (l + r) // 2
    #         if nums[m] > nums[m + 1]:
    #             return nums[m + 1]
    #         elif nums[m] > leftmost:
    #             l = m + 1
    #         else:
    #             r = m

    #     return -1
    
    # More elegant solution
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]