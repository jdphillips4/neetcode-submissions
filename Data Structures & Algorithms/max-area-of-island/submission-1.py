class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as previous, but now track maxArea
        # when bfs on a node finishes return how many it saw
        # then max it with maxArea, everything else same as prev

        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = 0

        directions = [[1,0], [-1,0], [0, 1], [0,-1]]

        def bfs(r, c):
            # while queue pop, check, iterate
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and 
                        (r, c) not in visited and 
                        grid[r][c] == 1):
                        queue.append((r, c))
                        visited.add((r, c))

        # then apply to grid
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and 
                    grid[r][c] == 1):
                    prev = len(visited)
                    bfs(r, c)
                    area = len(visited) - prev
                    maxArea = max(maxArea, area)
        
        return maxArea
