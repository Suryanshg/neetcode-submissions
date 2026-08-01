# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Returns the max path sum without splitting
    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0

        # Get max path sum of left and right subtrees
        # Taking max against 0 insures no negative values are used
        left_max = max(self.dfs(node.left), 0)
        right_max = max(self.dfs(node.right), 0)

        # Compute max path sum without splitting
        self.result = max(node.val + left_max + right_max, self.result)

        # Return max path sum with splitting
        return node.val + max(left_max, right_max)





    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val # root is guaranteed to be Non Null
        self.dfs(root)
        return self.result
        