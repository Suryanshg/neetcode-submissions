# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            # If both p and q have smaller values than current node
            # we search left of cur
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left 
            
            # If both p and q have greater values than current node
            # we search right of cur
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right

            # Otherwise, either p and q are in diff subtrees OR
            # p's or q's val is equal to current node
            # and in both cases, the current node is the lowest common ancestor 
            else:
                break

        return cur