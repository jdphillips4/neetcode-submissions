class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #use lengths to advantage and check first an last of rows
        # start in middle
        
        #easier to just bst the first of each row to find which row its in then bst that row
        #Rows = number lists, cols = length each list
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Bst on rows
        top, bot = 0, ROWS -1
        while top <= bot: 
            row = (top + bot ) //2
            if target > matrix[row][-1]: #last of row
                top = row +1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        
        if not (top <= bot):
            return False

        row = (top + bot ) // 2

        #bst on row
        l, r = 0, COLS - 1
        while (l<=r):
            mid = (l + r) // 2
            if matrix[row][mid] < target: 
                l = mid +1 
            elif matrix[row][mid] > target: 
                r= mid -1
            else:
                return True
        return False


        # midArr = len(matrix[0]) // 2
        # midMat = len(matrix) //2
        
        # mid = matrix[middMat][midArr]  #middle element
        # l = matrix[0][0] #first element
        # r = matrix[len(matrix)-1][len(matrix[0])-1] # last element

        # #Bst
        # while (l<=r):
        #     if mid < target: 
        #         l = mid +1 
                
        #     elif mid > target: 
        #         r= mid -1
        #     else
        #         return True
        # return False
        