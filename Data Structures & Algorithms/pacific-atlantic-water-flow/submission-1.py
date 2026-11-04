class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # optimal: start from ocean
        directions = [(-1, 0), (0, -1), (1, 0), (0,1)]
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        # visit can be p or a, 
        def dfs(r, c, visit, prevHeight):
            # counter if, return
            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                (r, c) in visit
                or prevHeight > heights[r][c]):
                return
            # add to visited and recurse all directions
            visit.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visit, heights[r][c])


        # starting points top and bottom 
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS -1])

        # starting points left and right
        for c in range(COLS): 
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS -1, c, atlantic, heights[ROWS-1][c])

        

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) in pacific and (r, c) in atlantic):
                    res.append([r, c])
        return res