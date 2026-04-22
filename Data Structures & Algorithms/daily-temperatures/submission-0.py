class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        #brute force start at i then iterate until greater, 
        # add distance to result then i++, would be O(n^2)

        # keep max heap for each i
        # min heap might be more useful
        # keep track of visited with smallest on top val, index
        
        stack = [] # pairs: [temp,index]
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #[-1][0] gives value at end of stack and first value in that pair
                stackT, stackIdx = stack.pop()
                result[stackIdx] = (i-stackIdx)
            stack.append([temp, i])
    
        return result