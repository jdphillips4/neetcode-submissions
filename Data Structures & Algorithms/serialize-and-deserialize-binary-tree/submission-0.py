# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # add nulls to help, use comma delimiter
        res = []

        def dfs(node):
            # base case
            if not node: # found null
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res) # put together w comma delimeter
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",") # split by comma
        self.i = 0 # global variable

        def dfs():
            if vals[self.i] == "N":
                self.i +=1
                return None
            # else make new node with val self.i
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs() 
            node.right = dfs()
            return node
        return dfs()

# basically have base case of finding a null, else add val, comma delimeter, 
# recurse left then right