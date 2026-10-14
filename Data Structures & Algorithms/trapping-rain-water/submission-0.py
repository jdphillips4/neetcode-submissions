class Solution:
    def trap(self, height: List[int]) -> int:
        # return area
        # up down up to store water
        # 2 ptrs that look for 2 maximums and store area between
        if not height:
            return 0
        # track maxima
        # values in between store difference with lowest maxima
        # trapped = max(0, min(leftMax, rightMax) - thisHeight)

        # could iterate and store leftMax going forward
        # and rightMax iterating backward in n time
        # then do min of these and substract height i as iterate again
        # this has added O(n) storage, 2 ptr can be better:
        
        trapped = 0
        l = 0
        r = len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        
        # greedy: move smaller one since want min(maxLeft,maxRight)
        # dont even need to do min function because greedy its 
        # maxLeft or l and vv
        while l<r:
            if height[l] <= height[r]:
                # use l as current then increment it
                l += 1
                maxLeft = max(maxLeft, height[l])
                trapped += max(0, min(maxLeft, maxRight) - height[l])
            elif height[l] > height[r]:
                # use r as curr
                r -=1
                maxRight = max(maxRight, height[r])
                trapped += max(0, min(maxLeft, maxRight) - height[r])

        return trapped

        