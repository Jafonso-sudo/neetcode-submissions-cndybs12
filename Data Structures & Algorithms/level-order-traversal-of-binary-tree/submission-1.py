# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution: BFS
# - Create a queue that processes node, left, right
# - Keep track of the current level we're at
# - Add to the queue the node and it's level

# Note:
# - Can be done w/ DFS recursion, but less elegant imo

class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     q = deque()
    #     q.append((root, 0))
    #     res = []

    #     while q:
    #         cur_node, cur_lvl = q.popleft()
    #         if cur_node == None:
    #             continue
    #         if cur_lvl >= len(res):
    #             res.append([])
    #         res[-1].append(cur_node.val)
    #         q.append((cur_node.left, cur_lvl + 1))
    #         q.append((cur_node.right, cur_lvl + 1))

    #     return res
        
    # Alternative: Instead of storing the current level, process level by level
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []

        while q:
            lvl_length = len(q)
            level = []
            for _ in range(lvl_length):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level)

        return res
