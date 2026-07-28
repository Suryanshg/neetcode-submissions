# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if node is None:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_arr = self.dfs(root)
        return sorted_arr[k-1]
