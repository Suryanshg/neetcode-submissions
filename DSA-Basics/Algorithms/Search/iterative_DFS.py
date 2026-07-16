from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_dfs(root: Optional[TreeNode]) -> List:
    if not root:
        return []
    
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# TODO: SUPER HARD TO UNDERSTAND
def in_order_dfs(root: Optional[TreeNode]) -> List:
    stack = []
    result = []
    current = root

    while current or stack:

        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left

        # Pop the current element
        current = stack.pop()
        result.append(current.val)
        
        # Move to its right subtree
        current = current.right



# NOTE: This is reverse of Root -> Right -> Left (Modified pre order)
def post_order_dfs(root: Optional[TreeNode]) -> List:
    if not root:
        return []
    
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)
    
    return result[::-1]  # Reversed becomes Left -> Right -> Root