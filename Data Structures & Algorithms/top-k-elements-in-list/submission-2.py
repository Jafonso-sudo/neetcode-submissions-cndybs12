# Option 1: O(n) Time, O(1) "O(R)" Space
# - Create a counter in a hashmap (or just fixed length list)
# - Iterate through numbers to fill counter -- O(n)
# - Sort counter by the value it's holding -- O(R) R=2000 -> O(1)
# - Return the first k

# Option 2: O(n) Time, O(n) Space
# - Similar, but create buckets for each seen number

# Cheatsheet
# - int constructor initializes to 0

# Bugs
# - lambda _ : 0 -> lambda : 0
# - sorted(..., ...) -> sorted(..., key=...)
# - key=x[1] -> key=-x[1]

# https://gemini.google.com/app/97ef83993c01a947

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = defaultdict(lambda : 0) # int would work but less readable
#         for num in nums:
#             counter[num] += 1

#         sorted_counter = sorted(list(counter.items()), key=lambda x: -x[1])

#         return [sorted_counter[i][0] for i in range(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        sorted_counter = sorted(counter.items(), key=lambda x: x[1])

        return [num for num, _ in sorted_counter[-k:]]

# Bucket Sort Approach
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # 1. Count frequencies: O(n)
#         # Counter is the Pythonic way to do your defaultdict(int) loop
#         freq_map = Counter(nums) 
        
#         # 2. Create buckets where index = frequency: O(n)
#         # We need n + 1 buckets (0 to n)
#         buckets = [[] for _ in range(len(nums) + 1)]
        
#         for num, freq in freq_map.items():
#             buckets[freq].append(num)
            
#         # 3. Gather top k elements: O(n)
#         result = []
#         # Iterate backwards from max possible frequency
#         for i in range(len(buckets) - 1, 0, -1):
#             for num in buckets[i]:
#                 result.append(num)
#                 if len(result) == k:
#                     return result
                    
#         return result