# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, target_node: TreeNode) -> List[TreeNode]:
        curr = root
        path = []
        while curr:
            path.append(curr)
            if curr.val == target_node.val:
                break
            elif target_node.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return path

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        path_p = self.dfs(root, p)
        path_q = self.dfs(root, q)

        result = root
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val:
                result = path_p[i]

        return result