# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution: DFS
# - Do DFS, left, node, right
# - Keep track of the number of nodes visited so far
# - Once we're at node k we update the result variable
# - If we're past k we just return

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def ksmall(node: Optional[TreeNode], i: int) -> int:
            nonlocal res
            if not node:
                return i
            
            # Search left
            i = ksmall(node.left, i)
            # Check self
            i += 1
            if i == k:
                res = node.val
            # Check right
            if i < k:
                i = ksmall(node.right, i)

            return i

        ksmall(root, 0)
        
        return res
        