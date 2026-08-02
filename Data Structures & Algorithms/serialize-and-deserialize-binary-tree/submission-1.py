# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Init result to be empty array
        result = []

        # Preorder Traversal DFS
        def dfs(node: TreeNode) -> str:
            # if Null node is reached, add "N" and exit
            if node is None:
                result.append("N")
                return

            # otherwise add the value of current node
            result.append(str(node.val))

            # run on left and right
            dfs(node.left)
            dfs(node.right)

        # run on the whole tree starting from root
        # this will populate the global variable result
        dfs(root)

        # Convert to string by joining using "," delimiter
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the data into a list using "," delimiter
        data_list = data.split(",")

        # Global index
        self.i = 0

        # Preorder Traversal DFS
        def dfs() -> TreeNode:

            # If at current index, its "N"
            # Then return Null Node and increment index
            if data_list[self.i] == "N":
                self.i += 1
                return None
            
            # Otherwise create a new Node using the value at current index
            node = TreeNode(int(data_list[self.i]))

            # Increment the index
            self.i += 1

            # Perform Preorder DFS and obtain left subtree
            # This will run to the depth of the left subtree (until dead end is encountered)
            node.left = dfs()

            # Perform Preorder DFS and obtain right subtree
            # This will run to the depth of the right subtree (until dead end is encountered)
            node.right = dfs()

            # Return the node with its left and right subtrees created
            return node

        # Run the algo starting with initial index 0
        return dfs()
        
