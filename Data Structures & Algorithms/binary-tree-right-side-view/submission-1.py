# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution:
# - Do BFS, go level by level, select the last node in each level
# - Alternative: (Less Clean imo) Do DFS always visiting right child first so that first node we reach at every depth is the visible right-side nodde

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        while q:
            lvl_len = len(q)
            lvl_last = None
            for _ in range(lvl_len):
                if cur := q.popleft():
                    lvl_last = cur.val
                    q.extend([cur.left, cur.right])
            if lvl_last is not None:
                res.append(lvl_last)
        
        return res