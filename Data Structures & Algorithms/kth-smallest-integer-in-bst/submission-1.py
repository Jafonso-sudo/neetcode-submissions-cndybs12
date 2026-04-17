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

# Cheatsheet
# - Morris Traversal of BST O(1) Space (second solution below) IF we are allowed to temporarily modify the input, otherwise still O(H)
#   https://gemini.google.com/app/2af2a061c8c3eb3a

class Solution:
    # DFS
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
    
    # Morris Traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            # If not left child, visit self, then move to right child next (or the thread if no right child exists)
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            # Else, find the inorder predecessor (rightmost node in left subtree)
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                # Create a temporary thread from inorder predecessor back to curr, then move to left child next
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                # If there's already such a thread, visit current node, then move to the right child of curr next
                else:
                    pred.right = None
                    k -= 1
                    if k== 0:
                        return curr.val
                    curr = curr.right
        