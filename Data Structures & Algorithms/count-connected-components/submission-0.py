class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs or bfs on a node, do it again until all seen
        #adj list, visited, dfs, each node if not vist dfs

        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2) #remember to append not set =
            adjList[n2].append(n1)
        
        visited = set()
        def dfs(node):
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res +=1

        return res
