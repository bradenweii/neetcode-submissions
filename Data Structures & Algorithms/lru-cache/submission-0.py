class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.cap = capacity

        self.left = Node()
        self.right= Node()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev=node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self,node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        node = self.m[key]

        self.remove(node)
        self.insert(node)

        return node.value




    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            self.remove(node)
        
        node = Node(key,value)
        self.insert(node)
        self.m[key] = node

        if len(self.m)>self.cap:
            node = self.left.next
            self.remove(node)
            del self.m[node.key]
        


