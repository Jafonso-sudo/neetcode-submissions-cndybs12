# Notes
# - This exercise just drained me. I didn't feel like working on it. It's not particularly hard, but it's so annoying thinking of the division of cases you have to consider...
# - Interesting point by Gemini review: if there were duplicates, this would go to O(n)

# BUG
# - Initially was just checking target/nums[m] <= nums[-1] (without the <= nums[0])
#.  In the case that there was no rotation (i.e. nums[-1] is the max), this was breaking.

# https://gemini.google.com/app/36faa4e742ccf325

# class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     l, r = 0, len(nums)

    #     while l < r:
    #         m = (l + r) // 2
            
    #         if nums[m] == target:
    #             return m
            
    #         # If they're in different "quadrants" move towards right quadrant
    #         if target <= nums[-1] <= nums[0] and nums[m] >= nums[0]:
    #             l = m + 1
    #         elif nums[m] <= nums[-1] <= nums[0] and target >= nums[0]:
    #             r = m
    #         # If they're in the same quadrant
    #         elif nums[m] < target:
    #             l = m + 1
    #         else:
    #             r = m
        
    #     return -1

    # Gemini
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the Left half is perfectly sorted
            if nums[left] <= nums[mid]:
                # Is the target within this strictly sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is here, discard right
                else:
                    left = mid + 1   # Target not here, discard left
            
            # Otherwise, the Right half MUST be perfectly sorted
            else:
                # Is the target within this strictly sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is here, discard left
                else:
                    right = mid - 1  # Target not here, discard right
                    
        return -1