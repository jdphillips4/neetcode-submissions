class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # window size k moves, each step return max
        # scanning window each time is O(k*(n-k))
        # how to minimize repeated work?
        # keep deque always decreasing, pop all if find greater
        # monotonically decreasing queue, add/remove O(1) -> O(n) solution


        res = []
        queue = collections.deque() # store indices

        l = 0
        r = 0
        while r < len(nums):
            # while q nonempty and rightmost < inserting
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
             # left out of bounds, remove left fro window
            if l > queue[0]:
                queue.popleft()
            # edge case
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r +=1
        return res
