class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # all distinct solutions = backtracking
        # each queen unique row, col, pos diag, neg diag
        
        # base case: 
        # choices: queen here or not

        #place in row, move to next row constrain diags and cols
        # choice is col in row to put it in decisions tree has index
        #use sets to constrain
        res = [] # list of boards

        cols = set() #set holds one of each no freqs
        posDiag = set() # / (r+c) 0,1 same as 1, 0
        negDiag = set() # \ (r-c) 0,1 same as 1, 2
        
        board = [["."]*n for i in range(n)]
        

        def backtrack(r): # row by row so use r, until n
            # base case on row n
            if r == n:
                # each row a string not an array, need to convert a to s
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
                
                # which position in row can place Q in
            for c in range(n):
                # if can place queen there
                if (c not in cols and
                    r + c not in posDiag and
                    r - c not in negDiag):
                    # update sets
                    cols.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)

                    board[r][c] = "Q"
                    backtrack(r + 1)

                    #undo for next iteration
                    cols.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
        backtrack(0)
        return res
            
            
            
            
           