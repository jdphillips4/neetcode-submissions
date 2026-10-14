class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # dont have to subtract inbetween heights
        # goal: maximize area
        # tallest and widest apart ideal
        # brute force: iterate every combo n^2

        # height = min of 2 chosen
        # width = right - left

        # pick 2 tallest, calc area, pick next tallest, etc. 
        # how do we avoid visiting every bar? 
        # left ptr right ptr if left+1 > left move it if right-1 > right

        maxArea = 0

        l = 0
        r = len(heights) -1 # last index

        while l<r:
            area = min(heights[l], heights[r]) * (r - l)

            maxArea = max(maxArea, area)

            # move ptr with smaller value, this is whats cuts time
            if heights[l] > heights[r]:
                r -=1
            elif heights[l] <= heights[r]:
                l += 1
                
        return maxArea