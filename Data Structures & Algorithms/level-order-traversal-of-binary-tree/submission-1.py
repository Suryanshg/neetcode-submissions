# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If root is null, return empty list
        if root is None:
            return []

        # Init current level with root node
        level = [root]

        # Init empty list as result
        result = []

        # current level has nodes
        while level:

            # Accumulate results for current level
            level_result = []
            next_level = []

            # For each node in current level
            for node in level:

                # Add the node's val in the current level's result
                level_result.append(node.val)

                # Add left and right node in the next level (if they exist)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # Add the current level result to main result list
            result.append(level_result)

            # Move current level to next level
            level = next_level
        
        # Return the result
        return result