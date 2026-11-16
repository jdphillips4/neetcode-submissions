class MedianFinder:
    # small heap  <= large heap, size difference 1
    # add/remove logn 
    # max heap find max is O(1)
    # small max, large min
    # whichever is bigger, return that max/min
    # otherwise its average of both
    
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) 
        # python only min heaps, do max heap by * -1
        
        # make sure every num small is <= every num in large
        if (self.small and self.large and (-1* self.small[0]) > self.large[0]):
            # pop small add to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven size?
        if (len(self.small) > len(self.large) + 1):
            # pop small add to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if (len(self.large) > len(self.small) + 1):
            # pop large push small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
        