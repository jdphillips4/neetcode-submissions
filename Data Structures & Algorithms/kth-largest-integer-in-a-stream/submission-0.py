class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minheap of size k
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        # nlogn

    def add(self, val: int) -> int:
        # add to heap then pop from heap to keep it size k
        # logn
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
