"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned_nodes = {}

        def dfs(current_node):
            if current_node in cloned_nodes:
                return cloned_nodes[current_node]

            cloned_node = Node(val = current_node.val)
            cloned_nodes[current_node] = cloned_node
            for neighbor_node in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor_node))
            return cloned_node
                
        return dfs(node) if node else None