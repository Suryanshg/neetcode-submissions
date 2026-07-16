# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If node is Null, return null
        if root is None:
            return root

        # Otherwise
        else:

            # Swap left and right nodes
            root.left, root.right = root.right, root.left
            
            # Recursively apply inversion on left and right subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)

            # Return the original head
            return root
