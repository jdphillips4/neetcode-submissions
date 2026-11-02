"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # given a node, visit node clone it visit neighbors
        # hashmap maps old to cloned
        # dfs on node checks if its in hashmap or adds it
        # then copies neightbors and dfs on them

        oldToNew = {}

        def dfs(node):
            # already cloned node
            if node in oldToNew:
                return oldToNew[node]

            # make clone and add it
            copy = Node(node.val)   
            oldToNew[node] = copy
            # add neighbors and recurse on them
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node) if node else None