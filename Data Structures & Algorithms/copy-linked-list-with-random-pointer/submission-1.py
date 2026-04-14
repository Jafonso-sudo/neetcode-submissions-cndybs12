"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Note: Solution also considers a way to avoid using a hashmap by interleaving the original and copies or by interleaving original and copy, but it's a bit hacky and I thought it unnecessary

class Solution:
    # This could be done slightly more elegantly by using a defaultdict to create the new never-accesed nodes, but it's fine
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}
        original = head
        while head:
            if head not in nodes:
                nodes[head] = Node(head.val, head.next, head.random)
            if head.next and head.next not in nodes:
                nodes[head.next] = Node(head.next.val, head.next.next, head.next.random)
            if head.random and head.random not in nodes:
                nodes[head.random] = Node(head.random.val, head.random.next, head.random.random)
            nodes[head].next = nodes[head.next]
            nodes[head].random = nodes[head.random]

            head = head.next
        
        return nodes[original]