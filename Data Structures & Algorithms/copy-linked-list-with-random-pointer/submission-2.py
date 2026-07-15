"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize Copy Map to store copies of each node
        # Init with Null Node whose copy would be another Null node
        copy_map = {None: None}

        # Create copies of each node
        ptr = head
        while ptr:
            copy = Node(ptr.val)
            copy_map[ptr] = copy
            ptr = ptr.next
        

        # For each node in the original LL
        # Set the copy node's next and random based on retrieval from
        # the copy map.
        ptr = head
        while ptr:
            # Get copy of current node
            copy = copy_map[ptr]

            # Using next and random of ptr
            # search for their copies in the map
            # Set those to be next and random of copy node
            copy.next = copy_map[ptr.next]
            copy.random = copy_map[ptr.random]

            # Move forward
            ptr = ptr.next

        # Return the copy of head
        return copy_map[head]