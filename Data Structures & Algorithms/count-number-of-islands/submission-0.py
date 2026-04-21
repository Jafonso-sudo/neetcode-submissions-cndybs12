# Solution: This can be done easily w/ BFS/DFS whilst keeping track of how many times we have to reset
# However, to review UnionFind, I went with that approach instead.

# Cheatsheet
# - With NeetCode's DSU(num_cells): dsu.union(index_first, index_second) returns True if successful or False if they are already in the same

class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        CHECK = [lambda i, j: i >= 0, lambda i, j: i < n, lambda i, j: j >= 0, lambda i, j: j < m]

        num_islands = 0
        union_find = DSU(n * m)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    num_islands += 1
                    idx_cur = i * m + j
                    for neigh, is_valid in zip(DIR, CHECK):
                        ii, jj = neigh
                        ii += i
                        jj += j
                        if not is_valid(ii, jj) or grid[ii][jj] == "0":
                            continue
                        idx_neigh = ii * m + jj
                        if union_find.union(idx_cur, idx_neigh):
                            num_islands -= 1
        
        return num_islands
                        