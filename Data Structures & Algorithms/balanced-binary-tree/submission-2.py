# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Returns a Tuple (isBalanced, depth)
    def dfs(self, curr) -> Tuple[bool, int]:
        # Base Case (curr is None)
        if not curr:
            return (True, 0)
        
        # Recursive Step
        # Perform this custom DFS on left and right subtrees
        left_tuple, right_tuple = self.dfs(curr.left), self.dfs(curr.right)

        # Compute is_balanced
        # If anything of the left and right subtrees are unbalanced, this bool
        # statement will get shortcircuited
        is_balanced = (left_tuple[0] and # If Left subtree is balanced
                        right_tuple[0] and # If right subtree is balanced
                        abs(left_tuple[1] - right_tuple[1]) <= 1) # If diff between left and right heights doesn't exceed 1
        
        # Return is_balanced and height
        return [is_balanced, 1 + max(left_tuple[1], right_tuple[1])]


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
        