# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Notes
# - Was thinking this was harder than it was, because I hadn't seen Example 2 (which in my interpretation would have evaluated to True)

# Cheatsheet
# - This still does require a fancy new algorithm that checks if a string is a substring of another in O(n + m) time. The Z-Algorithm.
#   https://www.geeksforgeeks.org/dsa/z-algorithm-linear-time-pattern-searching-algorithm/
# - I got to the point where I understand it, but still need to internalize it. However, if I had to explain it very simply:
# - We concatenate the string we're looking for and the string in which we want to look
# - We want to fill an array z, where z[i] = x means that the first x characters of the string match characters i : i + x (i.e. the prefix of length x)
# - Because we start with the array we're looking for, we check for potential prefixes in the target array itself, which enable us to not be so brute-force later

# Bug
# - Serialize wasn't returning after None
# - Serialize wasn't appending the value itself....

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        
        def to_list(data: list[Optional[int]], tree: Optional[TreeNode]):
            if not tree:
                data.append(None)
                return
            data.append(tree.val)
            to_list(data, tree.left)
            to_list(data, tree.right)
        
        data = []
        to_list(data, subRoot)
        m = len(data)
        to_list(data, root)
        n = len(data)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                k = i - l
                z[i] = min(r - i + 1, z[k])
            
            while i + z[i] < n and data[z[i]] == data[i + z[i]]:
                z[i] += 1
            
            if i >= m and z[i] >= m:
                return True
            
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        
        return False

        