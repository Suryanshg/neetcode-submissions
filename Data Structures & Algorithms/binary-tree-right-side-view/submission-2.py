# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If its an empty tree, return empty list
        if root is None:
            return []

        # Init result as empty
        result = []

        # Starting with current level of containing root node
        level = [root]

        # While current level has elements
        while level:

            # Determine next level
            next_level = []

            # for every node in current level
            for node in level:
                # Add left and right child nodes if they exist
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # Take current level's last element and add it to the result
            result.append(level[-1].val)

            # Move level to next level
            level = next_level

        # return result
        return result




        