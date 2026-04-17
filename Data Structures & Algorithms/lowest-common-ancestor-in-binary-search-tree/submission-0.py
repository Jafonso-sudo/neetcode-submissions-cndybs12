# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution:
# - Do DFS recursively that returns two booleans (one for each of the nodes we're looking for)
# - We search if the current node has one of them, or if the children have one of them
# - The first time we see that we have both we update our answer

# Bug
# - Was forgetting to return the intermediate findings
# - Was forgetting to actually call the recursive function

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def lca(node: TreeNode) -> tuple[bool, bool]:
            nonlocal res, p, q
            if not node:
                return False, False

            left_p, left_q = lca(node.left)
            right_p, right_q = lca(node.right)
            has_p = node.val == p.val or left_p or right_p
            has_q = node.val == q.val or left_q or right_q

            if has_p and has_q and not res:
                res = node
            return has_p, has_q

        lca(root)

        return res
