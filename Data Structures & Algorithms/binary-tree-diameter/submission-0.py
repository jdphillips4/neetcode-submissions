# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max of sums left and right height of nodes in the tree
        # need to track max diameter and heights
        self.maxDiam = 0 # creates member variable to be used in nested function
        #returns height
        def dfs(curr):
            if not curr: return 0

            left, right = dfs(curr.left), dfs(curr.right)

            height = 1 + max(left, right)

            self.maxDiam = max(self.maxDiam, left + right)

            return height

        dfs(root)
        return self.maxDiam

