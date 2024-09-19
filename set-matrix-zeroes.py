class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_Row_Zero = False
        first_Col_Zero = False
        rows,cols = len(matrix),len(matrix[0])
        for c in range(0,cols):
            if(matrix[0][c] == 0):
                first_Row_Zero = True
        for r in range(0,rows):
            if(matrix[r][0] == 0):
                first_Col_Zero = True
        for r in range(1,rows):
            for c in range(1,cols):
                if(matrix[r][c]==0):
                    matrix[r][0]=0
                    matrix[0][c] = 0
        for r in range(1,rows):
            if(matrix[r][0]==0):
                for c in range(1,cols):
                    matrix[r][c]=0
        for c in range(1,cols):
            if(matrix[0][c]==0):
                for r in range(1,rows):
                    matrix[r][c]=0
        if(first_Row_Zero):
            for i in range(0,cols):
                matrix[0][i]=0
        if(first_Col_Zero):
            for i in range(0,rows):
                matrix[i][0]=0
        

        
