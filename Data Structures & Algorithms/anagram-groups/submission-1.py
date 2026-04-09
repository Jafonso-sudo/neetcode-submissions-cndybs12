# Option 1: O(n^2 * l) Time, O(n) Space
# - Double for loop O(n^2), check if a string is an anagram of another in O(l) -> O(n^3)

# Option 2: O(n log n * l + l log l)
# - Sort each string O(l log l)
# - Sort strings by length, secondarily by the string itself O(n log n * l)
#  (Which simplifies to just by the string itself since I think they might be sorted like that?)
# DUMB /\

# Option 3: O(n * l)
# - Iterate through the strings O(n)
# - Count the letters in each O(l)
# - Put string in hash map with key equal to counter O(1) --- porportional to # of english letters
# - At the end, flatten the hash map

# Cheatsheet
# - Counter and list is not hashable, but tuple is (first build list, then convert to tuple)
# - Instead of original if/else logic, we can use a defaultdict(list) that automatically generates a value using a factory
# - Strings are sorted lexiographically (first letter, then second, etc...)
# - To sort strings by length first sorted(strs, key=lambda x: (len(x), x))
# - To sort indexes sorted_indexes = [i for i, val in sorted(enumerate(arr), key=lambda x: x[1])]

# class Solution:
#     def get_counter(self, s: str) -> tuple[int]:
#         counter = [0] * (ord('z') - ord('a') + 1)
#         for c in s:
#             counter[ord(c) - ord('a')] += 1
#         return tuple(counter)

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if not strs: return []

#         sorted_strs = {}

#         # O(n * l)
#         for s in strs:
#             s_counter = self.get_counter(s)
#             if s_counter in sorted_strs:
#                 sorted_strs[s_counter].append(s)
#             else:
#                 sorted_strs[s_counter] = [s]
        
#         return list(sorted_strs.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with lists
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # sorted(s) returns a sorted list of characters: ['a', 'c', 't']
            # We convert it to a tuple so it can be used as a dictionary key
            key = tuple(sorted(s))
            anagram_groups[key].append(s)
            
        return list(anagram_groups.values())