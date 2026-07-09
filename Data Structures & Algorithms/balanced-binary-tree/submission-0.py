# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, curr):
        if not curr:
            return 0
        return 1 + max(self.dfs(curr.left), self.dfs(curr.right))
        

        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        