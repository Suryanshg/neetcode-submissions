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
    return [root.val] + pre_order_dfs(root.left) + pre_order_dfs(root.right)


def in_order_dfs(root: Optional[TreeNode]) -> List:
    if not root:
        return []
    return in_order_dfs(root.left) + [root.val] + in_order_dfs(root.right)


def post_order_dfs(root: Optional[TreeNode]) -> List:
    if not root:
        return []
    return post_order_dfs(root.left) + post_order_dfs(root.right) + [root.val]


