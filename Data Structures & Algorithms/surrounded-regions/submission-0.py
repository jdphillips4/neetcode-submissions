class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # capture all surrounded regions  
        # connected O cells none touching edge
        # change all of these Os to Xs

        # brute: iterate thru look fo Os find all Os connected...

        # better: start from outside look for any Os and whats connected
        # then turn rest into Xs

        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # find all connected points and change to "T"
        def capture(r, c):
            # counter if
            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                board[r][c] != "O"):
                return
            # found another O
            board[r][c] = "T"
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                capture(nr, nc)

        # starting points with Os on edges
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)
        
        # final loop to modify board
        for r in range(ROWS):
            for c in range(COLS): 
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
# came up with solution, just needed help coding it out
# good: noticed it was easier to just see what was connected to border