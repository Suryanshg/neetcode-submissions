# Doubly-Linked List Node
# Store key - value
# Store prev and next pointers
# Doubly is needed since we will be removing elements so need to reference
# previous and next of the element removed
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity = 0
        self.cache = {} # For storing key-node pairs

        # Left = LRU, Right = MRU
        # left and right are dummy nodes
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Helper: Removes a given node
    def remove(self, node):
        # Get the prev and next of current node 
        prev, nxt = node.prev, node.next

        # Remove the node by
        # pointing prev's next to nxt
        # pointing nxt's prev to prev
        # Thus, reference of node is deleted
        prev.next, nxt.prev = nxt, prev

    # Helper: Insert at right
    def insert(self, node):
        # Retrieve the right's prev as prev and
        # right as next, wrt to node to be inserted
        prev, nxt = self.right.prev, self.right

        # Set prev's next and nxt's prev to be node
        prev.next = nxt.prev = node

        # Set node's prev and node's next to be prev and nxt, respectively
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        # If key exists in cache
        if key in self.cache:
            # Remove the related node
            # self.cache[key] gets the node at key
            self.remove(self.cache[key])

            # Reinsert at the right most position
            self.insert(self.cache[key])
            
            # Return its value
            return self.cache[key].val

        # Else return -1
        return -1


    def put(self, key: int, value: int) -> None:
        
        # If key already exists, remove the related node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new key-node pair in the cache
        self.cache[key] = Node(key, value)

        # Add the new node at the right most position
        self.insert(self.cache[key])

        self.capacity += 1

        # CAPACITY CHECK
        if len(self.cache) > self.max_capacity:
        # if self.capacity > self.max_capacity:

            # Get LRU node (left's next)
            lru = self.left.next

            # remove LRU from the LL
            self.remove(lru)

            # Delete the LRU (using its key) from the cache
            del self.cache[lru.key]

            self.capacity -= 1

