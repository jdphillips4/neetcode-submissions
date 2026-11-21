class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency list
        adjList = collections.defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))

        # Dijstras: BFS with priority queue minheap
        minHeap = [(0, k)] # total path, start node
        visited = set()

        heapq.heapify(minHeap)
        while minHeap:
            path, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return path
            for v, t in adjList[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (path + t, v))
        return -1