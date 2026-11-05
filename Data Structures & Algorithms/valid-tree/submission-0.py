class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid: connected, acyclic, n-1 edges
        # check for cycles, topological sort again 
        # adjacency list, dfs O(E + V)
        if not n:
            return True
        if len(edges) != n-1:
            return False
        
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        # will always find cycle because treating edges like directed
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjList[node]:
                if (neighbor == parent):
                    continue
                if (dfs(neighbor, node) == False): return False
            return True
    
        return dfs(0, -1) and len(visited) == n