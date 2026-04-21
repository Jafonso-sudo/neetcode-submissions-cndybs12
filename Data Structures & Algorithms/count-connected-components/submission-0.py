class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, idx: int) -> int:
        cur = idx
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, first: int, second: int) -> bool:
        first, second = self.find(first), self.find(second)
        if first == second:
            return False
        small, large = (first, second) if self.rank[first] <= self.rank[second] else (second, first)
        self.rank[large] += self.rank[small]
        self.parent[small] = large
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i, j in edges:
            if uf.union(i, j):
                n -= 1
        return n