# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# gemini: did the roleplay in 28 min total (pretty nice)
# - did the roleplay outside neetcode ui (did it in macos notes app) and still didn't have any syntax errors, pretty good!
# https://gemini.google.com/app/5aeaa04dd0576bf3

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
	
        def max_sum(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0
            left_best = max_sum(node.left)
            right_best = max_sum(node.right)

            single_path = max(left_best, right_best, 0) + node.val
            double_path = left_best + right_best + node.val
            res = max(res, single_path, double_path)

            return single_path

        max_sum(root)

        return res