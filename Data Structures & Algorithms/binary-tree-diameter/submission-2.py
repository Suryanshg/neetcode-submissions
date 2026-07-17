# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Helper Method That does DFS and returns height
    def dfs(self, curr):
        # If current node is None, return 0 as its height
        if not curr:
            return 0

        # Get height of left and right subtrees
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)

        # Calculate and Update max diameter
        # diameter = left height + right height
        self.max_diameter = max(self.max_diameter, left + right)

        # Return depth of this node
        # depth is 1 + max_depth(left, right)
        return 1 + max(left, right)
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Init a global variable to track max diameter so far
        self.max_diameter = 0

        # Perform DFS starting from root
        self.dfs(root)

        # Return the max diameter after the DFS execution
        return self.max_diameter



        
    
        