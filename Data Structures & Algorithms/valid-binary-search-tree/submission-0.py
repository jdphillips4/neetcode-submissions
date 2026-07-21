# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to track both left and right boundary
        def valid(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            # recurse on subtrees with updated boundaries
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right)) 
        
        return valid(root, float("-inf"), float("inf"))
        
        
        
        
        # #base case
        # if not root:
        #     return
        
        # # Check
        # # doesnt work 
        # if root.left.val and root.left.val > root.val:
        #     return False
        # if root.right.val and root.right.val < root.val:
        #     return False
        # #recursion
        # self.isValidBST(root.left)
        # self.isValidBST(root.right)

        # return True