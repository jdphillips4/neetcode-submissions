class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlogn for sorting, do better w heap which is O(n) then pop k times which is klogn
        # nums.sort()
        # return nums[len(nums)-k]
        # or do quick select which is average O(n) but worse case n**2
        maxHeap = [-n for n in nums]
        
        heapq.heapify(maxHeap)

        # pop k distinct times, track prev
        # prev = -maxHeap[0] +1 # make default prev different
        curr = -maxHeap[0]
        while k > 0:
            curr = -heapq.heappop(maxHeap)
            # if curr !=prev: # dont actually need to be distinct
            k-=1
            # prev = curr
        return curr
        