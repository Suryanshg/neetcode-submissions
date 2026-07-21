# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both are null
        if not p and not q:
            return True
        
        # If only 1 of them is null or their values are not same
        if not p or not q or p.val != q.val:
            return False

        # Compare the left trees together and the right trees together
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)