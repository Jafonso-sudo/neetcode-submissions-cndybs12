# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Notes
# - Should 1000% repeat this exercise. Really struggled with it. Might be that I was just a bit tired or expected something easier, but definitely good to repeat.
# - For an extra challenge, can do Morri's Traversal for O(1) extra space

# Cheatsheet

# In-Order Traversal
# Sequence: Left child → Root → Right child

# Pre-Order Traversal
# Sequence: Root → Left child → Right child
# The Root comes "Pre" (before) the children.

# Post-Order Traversal
# Sequence: Left child → Right child → Root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        pre_idx = in_idx = 0

        def tree(limit):
            nonlocal pre_idx, in_idx, n
            if pre_idx >= n:
                return None
            if inorder[in_idx] == limit:
                in_idx += 1
                return None
            
            node = TreeNode(preorder[pre_idx])
            pre_idx += 1
            node.left = tree(node.val)
            node.right = tree(limit)

            return node
        
        return tree(float('inf'))

            

