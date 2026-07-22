# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def areSameTrees(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        return self.areSameTrees(t1.left, t2.left) and self.areSameTrees(t1.right, t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If root is Null, return False
        if root is None:
            return False

        # Otherwise root exists, so we check if root and subroot are same trees or not
        if self.areSameTrees(root, subRoot):
            return True

        # Otherwise we check if root's left or root's right and subroot are same trees or not
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        