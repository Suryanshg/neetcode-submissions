# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Get Height
    def height_dfs(self, curr):
        if not curr:
            return 0

        left = self.height_dfs(curr.left)
        right = self.height_dfs(curr.right)

        self.max_diameter = max(self.max_diameter, left + right)
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.height_dfs(root)
        return self.max_diameter



        
    
        