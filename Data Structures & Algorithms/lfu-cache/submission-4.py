# Node for Doubly Linked List
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.freq = 1 # If a node is created, its freq must start with 1
        self.prev = None
        self.nxt = None


# Doubly Linked List
# Acts as a LRU cache
class LinkedList:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size


    def pushRight(self, node):
        # Get prev node of right
        prev = self.right.prev

        # Set Node to point to prev
        prev.nxt = node
        node.prev = prev

        # Set Node to point to right
        node.nxt = self.right
        self.right.prev = node
        self.size += 1


    def pop(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

        node.prev = node.nxt = None
        self.size -= 1


    def popLeft(self):
        if self.length() == 0:
            return None

        lru = self.left.nxt
        self.pop(lru)
        return lru


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> node
        self.lru_map = defaultdict(LinkedList) # freq -> LL
        self.lfu_count = 0
        self.capacity = capacity

    # Helper method to increase the counter
    def inc_counter(self, node):
        count = node.freq
        self.lru_map[count].pop(node)

        
        
        if count == self.lfu_count and self.lru_map[count].length() == 0:
            self.lfu_count += 1

        node.freq += 1
        self.lru_map[node.freq].pushRight(node)
        

        


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.inc_counter(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.inc_counter(node)
            return

        # If key not in cache, we are adding a new key
        # So we check for capacity and do eviction
        if len(self.cache) == self.capacity:
            # Remove the LRU from the LFU freq's bucket
            node = self.lru_map[self.lfu_count].popLeft()
            self.cache.pop(node.key)
        
        # Create a new key value pair
        node = Node(key, value)
        self.cache[key] = node
        self.lru_map[1].pushRight(node)
        self.lfu_count = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)