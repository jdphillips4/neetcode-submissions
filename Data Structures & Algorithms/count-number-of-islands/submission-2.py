class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            # is it a 1, is left right up or down a 1
            # dont need to check above if do dfs or something

            #look for a 1, do dfs, when popping make it 0
            # find 1, mark neighbor 1s visited, search for more islands

            if not grid:
                return 0
            
            ROWS = len(grid)
            COLS = len(grid[0])
            islands = 0
            visited = set() # set of (r, c)

            #write bfs
            def bfs(r, c):
                #while queue, popleft, check 1s in each direction
                queue = collections.deque() #deque() not deque
                queue.append((r, c))
                visited.add((r, c))

                while queue:
                    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if (r in range(ROWS) and
                            c in range(COLS) and
                            (r, c) not in visited and
                            grid[r][c] == "1"):
                            
                            visited.add((r, c))
                            queue.append((r, c))

            # now go through grid
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == "1" and (r, c) not in visited:
                        bfs(r,c) # should mark all connected 1s visited
                        islands +=1
            return islands

