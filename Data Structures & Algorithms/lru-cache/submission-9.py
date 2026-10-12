# Defines Node of a doubly linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # Maps key to LL node
        self.left = Node(0, 0) # Points at start of LL, its next will be LRU
        self.right = Node(0, 0) # Points at end of LL, its prev will be MRU
        self.left.nxt, self.right.prev = self.right, self.left

    # Helper Methods for managing Doubly LL
    def remove_node(self, node: Node): # Removes a node from the Doubly LL
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev 
        del node

    def insert_at_right(self, node: Node): # Inserts a node at the right most position
        prev, right = self.right.prev, self.right
        prev.nxt = right.prev = node
        node.prev = prev
        node.nxt = right

    # Main Methods
    def get(self, key):
        if key not in self.cache:
            return -1
        node: Node = self.cache[key]
        self.remove_node(node)
        self.insert_at_right(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove_node(self.cache[key])
    
        node = Node(key, value)
        self.cache[key] = node
        self.insert_at_right(node)


        # If capacity exceeds, evict LRU
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove_node(lru)
            del self.cache[lru.key]
        
