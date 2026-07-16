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


def in_order_dfs(root: Optional[TreeNode]) -> List:
    pass


def post_order_dfs(root: Optional[TreeNode]) -> List:
    pass