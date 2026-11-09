class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        # start at rottens =2, multistart bfs, track fresh fruit for -1
        # 1) starting points
        queue = collections.deque()
        fresh = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        # 2) BFS
        while queue and fresh > 0:
            # level order
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr in range(ROWS) and nc in range(COLS) and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1 # end of level
            
        return minutes if fresh == 0 else -1
