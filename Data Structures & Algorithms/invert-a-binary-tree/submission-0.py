# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        to_process = [root]
        while to_process:
            cur = to_process.pop()
            if not cur:
                continue
            cur.left, cur.right = cur.right, cur.left
            to_process.append(cur.left)
            to_process.append(cur.right)
        
        return root