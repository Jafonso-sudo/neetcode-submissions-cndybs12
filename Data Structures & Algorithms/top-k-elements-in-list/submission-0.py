# Option 1: O(n) Time, O(1) "O(R)" Space
# - Create a counter in a hashmap (or just fixed length list)
# - Iterate through numbers to fill counter -- O(n)
# - Sort counter by the value it's holding -- O(R) R=2000 -> O(1)
# - Return the first k

# Bugs
# - lambda _ : 0 -> lambda : 0
# - sorted(..., ...) -> sorted(..., key=...)
# - key=x[1] -> key=-x[1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(lambda : 0) # int would work but less readable
        for num in nums:
            counter[num] += 1

        sorted_counter = sorted(list(counter.items()), key=lambda x: -x[1])

        return [sorted_counter[i][0] for i in range(k)]