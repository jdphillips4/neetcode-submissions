class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # can a cell reach both upper left and lower right
        # dont care about distance just does path exist
        # adds position [r,c] to res if both paths exist
        # goes to neighbor if neighbor <= curr
        # an ocean would be if upper or left out of bounds = pacific
        # down or right out of bounds = atlantic found
        
        # dfs probably better because dont care about distance just looking for path
        # up, left, down, right= pacific, atlantic
        directions = [(-1, 0), (0, -1), (1, 0), (0,1)]
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        def dfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            
            visited = set()
            visited.add((r, c))
            
            pacific_found = (r == 0 or c == 0)
            atlantic_found = (r == ROWS - 1 or c == COLS - 1)

            while queue:
                row, col = queue.pop() # pop for dfs

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                
                    # pacific case
                    if (nr < 0 or nc < 0):
                        pacific_found = True
                        continue
                    # atlantic case
                    if (nr >= ROWS or nc >=COLS):
                        atlantic_found = True
                        continue
                    # explore neighbors
                    if ( (nr, nc) not in visited and 
                            heights[nr][nc] <= heights[row][col]):
                            # neighbor <= curr possible path
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                        
                if (pacific_found and atlantic_found):
                    res.append([r, c]) # only cell doing dfs on
                    return                    

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c) # should append to res
        
        return res

# my solution brute force O((nm)^2)
# can start from ocean then go in O(nm) and track visited
# is reversed so >=, track sets of what can reach each ocean also