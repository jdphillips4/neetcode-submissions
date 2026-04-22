class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = collections.defaultdict(set) #key: row number, val: set all values in row
        colMap = defaultdict(set)
        squareMap = defaultdict(set) #key: (row/3, col/3)

        # integer division gives whole number rounded down always
        # / vs //
        #default dict vs set vs {}
        for r in range(9): 
            for c in range(9):
                if board[r][c] == ".": continue
                #iterate row
                if board[r][c] in rowMap[r]: return False
                #iterate col
                if board[r][c] in colMap[c]: return False
                #iterate square
                if board[r][c] in squareMap[(r//3, c//3)]: return False

                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                squareMap[(r//3,c//3)].add(board[r][c])
        
        return True


        
