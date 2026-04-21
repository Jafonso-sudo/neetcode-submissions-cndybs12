# Solution: Check if any node is visited more than once, if it is, then we don't have a tree (else if they mean tree == there is a topological order, we do the classic)
# NOTE: Optimization: Valid tree must have n - 1 edges

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for i, j in edges:
            if i == j:
                return False
            adj[i].append(j)
            adj[j].append(i)
        
        stack = [(0, 0)]
        while stack:
            cur, prev = stack.pop()
            if visited[cur]:
                return False
            visited[cur] = True
            for neigh in adj[cur]:
                if neigh != prev:
                    stack.append((neigh, cur))
        
        for visit in visited:
            if not visit:
                return False
        
        return True

