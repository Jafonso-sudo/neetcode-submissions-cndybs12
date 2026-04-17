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

# DUMB
# - Didn't see this was specifically for a binary search tree. We can optimize.


class Solution:
    # Solution before realizing this was for binary search tree
    # Note
    # - Code goes for clean over optimized (could further optimize it by checking first if we go what we want after the first left call & also if we didn't use recursion, we could return as soon as we find what we want)
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     res = None

    #     def lca(node: TreeNode) -> tuple[bool, bool]:
    #         nonlocal res, p, q
    #         if not node:
    #             return False, False

    #         left_p, left_q = lca(node.left)
    #         right_p, right_q = lca(node.right)
    #         has_p = node.val == p.val or left_p or right_p
    #         has_q = node.val == q.val or left_q or right_q

    #         if has_p and has_q and not res:
    #             res = node
    #         return has_p, has_q

    #     lca(root)

    #     return res

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = (p, q) if p.val < q.val else (q, p)
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif p.val >= root.val:
                root = root.right
            else:
                root = root.left