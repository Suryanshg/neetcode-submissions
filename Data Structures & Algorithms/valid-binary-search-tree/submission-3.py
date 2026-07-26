# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, low, high):
        # return true if node is null
        if node is None:
            return True

        # check node and its left and right subtrees
        return (((node.val > low) and (node.val < high)) 
        and self.dfs(node.left, low, node.val)
        and self.dfs(node.right, node.val, high))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # run DFS check using -inf and +inf as low and high 
        return self.dfs(root, float("-infinity"), float("infinity"))
        