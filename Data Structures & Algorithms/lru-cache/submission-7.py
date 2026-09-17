class Node:
    """
    Node of a doubly linked list which also stores a key and a value.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache Implementation using Hash Map (Dict) and Doubly Linked List.
    Doubly Linked List allows to keep track of the most recent and least recently used values.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Maps: key -> Node(key, value)
        
        # Create two nodes: left and right 
        # left.next = LRU
        # right.prev = MRU
        # They are dummy nodes and initially pointing to each other
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        """
        Return the value of the corresponding key if it exists, otherwise -1.
        """
        # If key exists in cache
        if key in self.cache:
            # Retrieve the node
            # Reinsert it at the right most position
            self.remove_node(self.cache[key])
            self.insert_at_right(self.cache[key])

            return self.cache[key].value
        # Return -1 as default case
        return -1


    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if it exists, otherwise add the key-value pair
        in the cache. If introduction of the new pair causes the cache to exceed its capacity, remove
        the least recently used key.
        """
        # If key exists in cache
        if key in self.cache:
            # Retrieve the node and delete it (as it will be updated)
            old_node = self.cache[key]
            self.remove_node(old_node)
            # self.remove_node(self.cache[key])

        # Insert a new Node at the key using new value
        new_node = Node(key, value)
        self.cache[key] = new_node

        # Insert the new node at rightmost position in the Linked List
        self.insert_at_right(new_node)

        # If current length exceeds capacity, evict LRU from LL and cache
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]



    def remove_node(self, node: Node) -> None:
        """
        Removes the given node from the Double Linked List.
        """
        # Retrieve its prev and nxt nodes
        prev, nxt = node.prev, node.next

        # Set prev to point to nxt and nxt to point to prev
        prev.next, nxt.prev = nxt, prev

        # Delete the node in the memory
        # del node


    def insert_at_right(self, node: Node) -> None:
        """
        Inserts a node at the right most position in the Double Linked List.
        """
        # Retrieve the prev node of right
        prev, right = self.right.prev, self.right

        # We insert node between prev and right
        prev.next = right.prev = node
        node.prev, node.next = prev, right       
