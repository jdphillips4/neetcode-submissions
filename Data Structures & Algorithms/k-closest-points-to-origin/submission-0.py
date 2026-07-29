class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # apply distance to points then add to minheap then pop k times
        # def distance([xi,yi]):
        #     return sqrt((xi)^2 + (yi)^2)
            
        minHeap = []
        for x, y in points:
            dist = (x**2 + y**2) # dont actually need to sqrt by nature of problem
            minHeap.append([dist, x, y]) #python uses first value by default for minHeap
        
        heapq.heapify(minHeap)

        k_closest = []
        while k> 0:
            dist, x, y = heapq.heappop(minHeap)
            k_closest.append([x,y])
            k -=1
        
        return k_closest

        