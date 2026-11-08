class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)] # ith node -> parent (1-n)skip0
        rank = [1] * (N+1)

        def find(n):
            if n ==parent[n]:
                return parent[n]
            find(parent[n])
            parent[n] = find(parent[n])
            return parent[n]
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2) # find parent of n1n2
            if p1 == p2:
                return False # skip union
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for n1, n2 in edges:
            if not union(n1, n2): # if cant be unioned found cycle
                return [n1, n2]