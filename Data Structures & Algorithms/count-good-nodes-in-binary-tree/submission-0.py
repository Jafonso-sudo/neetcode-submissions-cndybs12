# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        s = [(root, float('-inf'))]
        while s:
            cur, cur_max = s.pop()
            # Base case
            if not cur:
                continue

            # Recursive call
            cur_max = max(cur_max, cur.val)
            if cur.val >= cur_max:
                res += 1
            s.append((cur.left, cur_max))
            s.append((cur.right, cur_max))
        
        return res