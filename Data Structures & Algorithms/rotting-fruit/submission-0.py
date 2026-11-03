class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 empty, 1 fresh, 2 rotten
        # horiz/vetical adjacent fresh rotten 1 min
        # min mins zero fresh, -1 if impossible

        # BFS starting from all rotten fruits
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = collections.deque()
        # can convert to 2 so dont need visited
        fresh = 0 # track this dont have to loop at end for -1 case

        # multistart, add all rotten fruits to queue
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 2):
                    queue.append((r, c))
                if (grid[r][c] == 1):
                    fresh += 1
        
        
        total_minutes = 0
        # BFS
        while queue and fresh > 0:
            layer_length = len(queue) # allows us to track each min
            
            for i in range(layer_length): # i is not used
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    # decide if its a fresh fruit turned rotten
                    if (r in range(ROWS) and 
                        c in range(COLS) and 
                        grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -=1 # fresh now rotten
                        queue.append((r, c)) # only appending new rotten
            # end of layer, see if added any,
            #dont need this if if have fresh>0 condition in while loop
            #if (len(queue) > 0):
            total_minutes +=1
            
        
        # check if any fresh fruit left to return -1
        if fresh > 0: 
            return -1
        
        return total_minutes

# to be faster can track fresh oranges from start then subtract as go through
# good job using length queue at start to track minutes

