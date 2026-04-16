# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_s, q_s = [p], [q]
        while p_s and q_s:
            p, q = p_s.pop(), q_s.pop()
            if not (p == q == None or (p and q and p.val == q.val)):
                return False
            if p == None:
                continue
            p_s.append(p.left)
            p_s.append(p.right)
            q_s.append(q.left)
            q_s.append(q.right)
            

        return not p_s and not q_s