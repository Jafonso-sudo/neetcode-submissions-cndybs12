# Solution
# - From comparing "neighbor" words construct a graph out of the letters
#   where x points to y if x preceeds y in the new ordering.
# - Now get a topological ordering for it (if one exists, else return "")
# - At the end we check if our topological ordering is complete

# n f
# h e
# r n
# e r

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        if len(words) == 1:
            return words[0]
        adj = [[] for _ in range(26)]
        in_num = [0] * 26
        seen = set()
        for i in range(len(words) - 1):
            left = words[i]
            right = words[i + 1]
            seen = seen.union(left)
            seen = seen.union(right)
            min_len = min(len(left), len(right))
            for j in range(min_len):
                if left[j] == right[j]:
                    if j == min_len - 1 and len(left) > len(right):
                        return ""
                    continue
                adj[ord(left[j]) - ord('a')].append(ord(right[j]) - ord('a'))
                in_num[ord(right[j]) - ord('a')] += 1
                break
        
        stack = [i for i in range(26) if not in_num[i] and chr(i + ord('a')) in seen]
        res = []
        while stack:
            cur_idx = stack.pop()
            if in_num[cur_idx] > 0 or in_num[cur_idx] <= -1:
                continue
            in_num[cur_idx] -= 1 # set as visited
            cur_chr = chr(cur_idx + ord('a'))
            res.append(cur_chr)

            for neigh_idx in adj[cur_idx]:
                in_num[neigh_idx] -= 1
                stack.append(neigh_idx)
        
        return "".join(res) if len(res) == len(seen) else ""

            