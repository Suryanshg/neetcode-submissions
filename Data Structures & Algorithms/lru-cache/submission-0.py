class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # For storing key-node pairs

        # Left = LRU, Right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove a given node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        if key in self.cache:
            # Remove the related node
            self.remove(self.cache[key])

            # Reinsert at the right most position
            self.insert(self.cache[key])
            
            # Return its value
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        
        # If key already exists, remove the related node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new key-node pair in the cache
        self.cache[key] = Node(key, value)

        # Add the new node at the right most position
        self.insert(self.cache[key])

        # CAPACITY CHECK
        if len(self.cache) > self.capacity:
            # Remove from list and delete the LRU from the dict
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

