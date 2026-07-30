# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If both preorder and inorder lists are empty, return null node
        if not preorder or not inorder:
            return None

        # Use the first value in preorder list to create root node
        root = TreeNode(preorder[0])

        # Find idx of root node in inorder list
        mid = inorder.index(preorder[0])

        # Recursively construct left subtree
        # preorder gets "mid" number of elements starting right after the root node
        # 
        # inorder gets all elements until mid as the mid points to root node's location
        # in the inorder array
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])


        # Recursively construct right subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])


        return root