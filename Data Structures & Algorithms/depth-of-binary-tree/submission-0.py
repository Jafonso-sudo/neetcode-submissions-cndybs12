# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0)]
        while stack:
            cur, depth = stack.pop()
            depth += 1
            if not cur:
                continue

            res = max(res, depth)
            stack.append((cur.left, depth))
            stack.append((cur.right, depth))
        
        return res