class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # loop thorugh until find land cell
        # DFS on land cell until find treasure, tracking length path
        # dont change from INF if dont find treasure
        # BFS better because intrinsically tracks minimum distance
        # do it from the chests
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        visited = set()
        queue = collections.deque()
        # starting points
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r,c))
        
        #BFS
        path = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = path
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and 
                        (nr, nc) not in visited and 
                        grid[nr][nc] != -1):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            path += 1
        
