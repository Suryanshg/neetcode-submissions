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
        copy_map = {None: None}
        ptr = head
        while ptr:
            copy = Node(ptr.val)
            copy_map[ptr] = copy
            ptr = ptr.next
        

        ptr = head
        while ptr:
            copy = copy_map[ptr]
            copy.next = copy_map[ptr.next]
            copy.random = copy_map[ptr.random]
            ptr = ptr.next

        return copy_map[head]