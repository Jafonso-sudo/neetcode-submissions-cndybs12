# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Gemini Roleplay 35 mins start to end
# - Had a few syntax errors
# - Also hadn't realized at first that we didn't really need level separators
# https://gemini.google.com/app/c627eb20e42aecc4

# Looking at the official solution I like their logic better for handling the parent connections

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur:
                res.append(str(cur.val))
            else:
                res.append("O")
                continue
            q.append(cur.left)
            q.append(cur.right)
        
        return ",".join(res)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        res = TreeNode()
        i = 0
        q = deque([(res, None)])
        while q:
            c = data[i]
            left, right = q.popleft()
            i += 1
            if c == "O":
                continue
            val = int(c)
            node = TreeNode(val)
            if left:
                left.left = node
            if right:
                right.right = node
            q.append((node, None))
            q.append((None, node))
          
        return res.left