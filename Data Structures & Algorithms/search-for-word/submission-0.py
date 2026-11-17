class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # look for all occurances of 1st letter, check surroundings until its not there
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        path = set() # make sure dont visit same twice
        # input r, c of first letter, search for full word
        def dfs(r, c, i):
            # Matched the entire word
            if i == len(word):
                return True
            # Out of bounds, already visited, or wrong character
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[i] or 
                (r, c) in path):
                return False
            path.add((r, c))
            
            res = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))

            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True
        
        return False
                