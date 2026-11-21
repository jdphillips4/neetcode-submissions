class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time is weighted distance times[i][2]
        # source u to target v weighted by time
        # k is start node
        # minimum 

        # can the signal travel outwardly at same time like BFS?
        # does it have to flow in one direction? i would think yes this one

        # trying to follow a path to reach all nodes and minimize this path

        # it actually is like the bfs version where its total wegihted distance from start node for each of them and then the maximum of that is what to we want to minimize

        # Dijstas: bfs with minheap
        # add layer to frontier(minheap), pop min 
        # (totalpath, node) 
        # return totalpath of final pop if all n nodes visited
        # edges= vertices^2 every heap operation logV^2, up to E
        # so O(2ElogV)

        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t)) # u to v weight t

        minHeap = [(0, k)] # start at k weight 0
        visited = set() 

        # BFS layer by layer: pop then add neighbors
        heapq.heapify(minHeap)
        while minHeap:
            totalPath, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return totalPath
            for v, t in edges[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (t + totalPath, v))
        return -1
            