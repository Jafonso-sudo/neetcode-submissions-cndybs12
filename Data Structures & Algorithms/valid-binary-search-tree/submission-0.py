# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution:
# - We do DFS, we keep track of the allowed range so far
# - Whenever we go right we update the minimum
# - Whenever we go left we update the max
# - We return False if the range is broken, otherwise True

# Bug
# - Originally was referencing the outside variable root instead of the inside node...

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            # Base Case
            if not node:
                return True
            elif not (min_val < node.val < max_val):
                return False
            
            # Recursive Case
            return bst(node.left, min_val, node.val) and bst(node.right, node.val, max_val)
        
        return bst(root, -1001, 1001)