# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS queue
        res = []

        queue = collections.deque()

        queue.append(root)
        # want to pop a node into a level, add its children to queue
        # keep track of length of each level before hand 
        while queue:
            lenQ = len(queue) #starts at 1
            level = []

            for i in range(lenQ):
                node = queue.popleft() #popleft vs pop
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        
        return res
