# Solution 1: O(n^2)
# - Get the numbers in a hash set O(n) (& their count)
# - Try every pair of numbers, check if the third is in the hash set

# Solution 2? O(n log n)?
# Sort first e.g. [-4, -1, -1, 0, 1, 2]
# - I couldn't think of something, going with Solution 1

# Notes
# - Really struggled coming up with a clean way to do combinations (I wanted to avoid the hashing the combinations)
# - This is an interesting problem, I should redo it at some point

# Cheatsheet
# - Do .sort() to do in-place sorting

# https://gemini.google.com/app/83d4e4cfef0d9951

class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     counter = defaultdict(int)

    #     for num in nums:
    #         counter[num] += 1

    #     unique_nums = sorted(counter.keys())
    #     result = []
    #     for i, first_num in enumerate(unique_nums):
    #         counter[first_num] -= 1
    #         start_j = i if counter[first_num] else i + 1
    #         for j in range(start_j, len(unique_nums)):
    #             second_num = unique_nums[j]
    #             counter[second_num] -= 1

    #             third_num = -first_num - second_num
    #             if third_num >= second_num and counter.get(third_num, 0) > 0:
    #                 result.append([first_num, second_num, third_num])

    #             counter[second_num] += 1
    #         counter[first_num] += 1

    #     return result
    
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     counter = defaultdict(int)

    #     for num in nums:
    #         counter[num] += 1

    #     result = set()

    #     unique_nums = list(counter.keys())
    #     for i, first_num in enumerate(unique_nums):
    #         counter[first_num] -= 1
    #         start_j = i if counter[first_num] else i + 1
    #         for j in range(start_j, len(unique_nums)):
    #             second_num = unique_nums[j]
    #             counter[second_num] -= 1

    #             third_num = -first_num - second_num
    #             if counter.get(third_num, 0) > 0:
    #                 triplet = tuple(sorted((first_num, second_num, third_num)))
    #                 if triplet not in result:
    #                     result.add(triplet)

    #             counter[second_num] += 1
    #         counter[first_num] += 1


    #     return [[i, j, k] for i, j, k in result]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, first_num in enumerate(nums):
            # Skip impossible triplet
            if first_num > 0:
                break
            # Skip duplicates
            if i > 0 and nums[i - 1] == first_num:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = first_num + nums[l] + nums[r]
                if three_sum < 0: l += 1
                elif three_sum > 0: r -= 1
                else:
                    result.append([first_num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result


        