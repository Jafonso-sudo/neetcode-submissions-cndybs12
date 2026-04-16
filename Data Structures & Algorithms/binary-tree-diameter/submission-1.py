# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Bugs
# - Base case was returning 0 instead of -1 (causing a single node to output 1)
# - Was forgeting to calculate best_left + best_right as one of the options

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def diameter(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return -1
            
            best_left = diameter(node.left) + 1
            best_right = diameter(node.right) + 1
            best_cur = max(best_left, best_right)
            best = max(best, best_cur, best_left + best_right)

            return best_cur
        
        diameter(root)

        return best
