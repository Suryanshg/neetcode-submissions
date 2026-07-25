# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: TreeNode, max_so_far: int = -100):
        # If a node is none, return 0 good nodes
        if node is None:
            return 0

        # Start with 0 good nodes detected
        good_nodes = 0

        # If the current node's value is atleast max_so_far
        # update max_so_far and add 1 to good nodes detected
        if node.val >= max_so_far:
            good_nodes += 1
            max_so_far = node.val
        
        # Search for good nodes in left and right subtrees and return total good nodes
        return good_nodes + self.dfs(node.left, max_so_far) + self.dfs(node.right, max_so_far)
        
        
    def goodNodes(self, root: TreeNode) -> int:
        # Run the custom good node counting dfs algo
        return self.dfs(root)
        