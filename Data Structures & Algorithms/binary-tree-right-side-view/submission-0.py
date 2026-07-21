# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # rightmost child, if no right check left
        # can do bfs, adding children to queue like normal
        # but then instead of popping all on a level only pop one 

        res = []

        queue = collections.deque()

        queue.append(root)

        while queue: 
            lenQ = len(queue)
            level = []

            for i in range(lenQ):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level[-1]) # only add last of level

        return res
