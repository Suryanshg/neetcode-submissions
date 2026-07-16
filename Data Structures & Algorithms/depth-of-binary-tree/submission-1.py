# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If node is Null, return 0
        if root is None:
            return 0
        
        # Otherwise
        else:
            # Count current node's depth (as + 1)
            # Find depth of left and right sub trees and find the max of them
            # Add max(left, right) + 1
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        