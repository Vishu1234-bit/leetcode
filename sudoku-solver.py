class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(board,row,col,num):
            num=str(num)
            for i in range(0,9):
                if(board[row][i]==num):
                    return False
                if(board[i][col]==num):
                    return False
                if(board[3*(row//3)+i//3][3*(col//3)+i%3]==num):
                    return False
            return True
        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if(board[row][col]=='.'):
                    for num in range(1,10):
                        if(isValid(board,row,col,num)):
                            board[row][col]=str(num)
                            if(self.solveSudoku(board)):
                                return True
                            board[row][col]='.'
                    return False
        return True

                        
