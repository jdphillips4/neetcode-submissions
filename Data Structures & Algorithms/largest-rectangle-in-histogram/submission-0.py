class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # largest area = maximize(min height of all around * length)

        # [7, 1, 7, 2, 2, 4]
        # 2*4 = 8

        # could start with full length *1 then move up to next min etc. 
        # go by minimums, 

        # look to right see how far then pop, only pop most recent so use stack
        # index, height if next height < this pop but track area when poppin g

        # extend back index and treat start as that index but with this height
        
        stack = [] # store (index, height)
        maxArea = 0

        for i, h in enumerate(heights): 
            start = i
            # while stack not empty and top value height > height just reached
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        # then go thorugh leftovers that made it to end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i) )
        return maxArea
