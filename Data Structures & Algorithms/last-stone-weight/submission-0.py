class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # insert all to maxHeap nlogn
        # no max heap in python so make all negative then minheap
        stones = [-s for s in stones]
        maxHeap = stones
        heapq.heapify(maxHeap)

        # simulate, each pop logn
        while len(maxHeap) > 1:
            first = (-1) * heapq.heappop(maxHeap) # biggest
            second = (-1) * heapq.heappop(maxHeap) # 2nd biggest

            if second < first:
                first = first - second
                heapq.heappush(maxHeap, -first)
            
        if maxHeap:
            return (-1) * maxHeap[0]  
        else:
            return 0
            