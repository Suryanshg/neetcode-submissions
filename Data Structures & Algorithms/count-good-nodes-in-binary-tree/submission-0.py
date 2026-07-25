# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: TreeNode, max_so_far: int = -100):
        if node is None:
            return 0

        good_nodes = 0
        if node.val >= max_so_far:
            print(node.val)
            good_nodes += 1
            max_so_far = node.val
        
        return good_nodes + self.dfs(node.left, max_so_far) + self.dfs(node.right, max_so_far)
        
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root)
        