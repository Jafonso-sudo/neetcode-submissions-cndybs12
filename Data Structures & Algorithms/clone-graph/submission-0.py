"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            if node in seen:
                return seen[node]
            
            neighbors = []
            seen[node] = Node(node.val, neighbors)
            for neigh in node.neighbors:
                neighbors.append(dfs(neigh))
            
            return seen[node]
        
        return dfs(node)


        