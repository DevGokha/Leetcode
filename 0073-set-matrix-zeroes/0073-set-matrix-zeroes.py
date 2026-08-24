class Solution:
    def setZeroes(self, martix: List[List[int]]) -> None:
        row = len(martix)
        cols = len(martix[0])
        first_row_zero = False
        first_col_zero = False

        for j in range(cols):
            if martix[0][j] == 0:
                first_row_zero = True

        for i in range(row):
            if martix[i][0] == 0:
                first_col_zero = True
        
        for i in range(1,row):
            for j in range(1,cols):
                if martix[i][j] == 0:
                    martix[i][0] = 0
                    martix[0][j] =0
        
        for i in range(1, row):
            if martix[i][0] ==0:
                for j in range(1, cols):
                    martix[i][j] =0

        for j in range(1, cols):
            if martix[0][j] == 0:
                for i in range(1,row):
                    martix[i][j] =0
        
        if first_row_zero:
            for j in range(cols):
                martix[0][j] =0


        if first_col_zero:
            for i in range(row):
                martix[i][0] = 0





        