# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # could dfs until find one of them look at each layer of parent 
        # seeing if can find other
        # root always ca
        # is bst didnt realize, split is LCA
        curr = root

        while curr: #while not null
            if p.val > curr.val and q.val > curr.val: #go down right subtree
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: # left subtree
                curr = curr.left
            else:
                return curr

# O(h) time, O(1) space
