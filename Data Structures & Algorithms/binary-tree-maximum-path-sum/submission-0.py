# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #max path can get from left subtree if dont end up splitting
        #can only split once
        res = [root.val]

        #return max path sum without splitting
        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            # account for negatives
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute max path sum WITH split
            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    # O(n) time, O(h) space