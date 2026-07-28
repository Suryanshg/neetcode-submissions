# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def in_order_dfs(self, node):
        # Node is Null, return empty list
        if node is None:
            return []
        
        # convert left subtree to list 
        # then add node.val
        # convert right subtree to list
        # extend them together
        return self.in_order_dfs(node.left) + [node.val] + self.in_order_dfs(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do in order dfs on BST
        # This returns a sorted array
        sorted_arr = self.in_order_dfs(root)
        
        # Return element at k - 1 idx in the sorted array
        return sorted_arr[k-1]
