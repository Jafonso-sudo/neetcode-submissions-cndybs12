# Solution:
# - Create a deque and a hashmap
# - Deque stores keys in the order they are used
# - Hashmap stores key, value, and reference to node in the deque

# Cheatsheet
# - Implementation for this deque w/ node access is much simpler with a dummy start and end node. Did not do that at first.

class Node:
    def __init__(self, key: int, prev: 'Node' | None = None, next: 'Node' | None = None) -> None:
        self.key = key
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

        self.prev = self.next = None

        return self.key
    
    def add_before(self, node: 'Node'):
        self.prev = node.prev
        self.next = node

        self.prev.next = self
        self.next.prev = self

class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.head, self.tail = Node(0), Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        value, node = self.data[key]

        node.remove()
        node.add_before(self.tail)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            _, node = self.data[key]
            node.remove()
        else:
            node = Node(key)
        
        node.add_before(self.tail)
        self.data[key] = (value, node)

        if len(self.data) > self.capacity:
            self.data.pop(self.head.next.remove())



        
