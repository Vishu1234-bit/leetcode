class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def solve(chess,row,lowerdiagonal,upperdiagonal,result,col):
            if(col==n):
                result.append([''.join(r) for r in chess])
                return
            for r in range(n):
                if(row[r]==0 and lowerdiagonal[r+col]==0 and upperdiagonal[n-1+(col-r)]==0):
                    chess[r][col]='Q'
                    row[r]=1
                    lowerdiagonal[r+col]=1
                    upperdiagonal[n-1+(col-r)]=1
                    solve(chess,row,lowerdiagonal,upperdiagonal,result,col+1)
                    chess[r][col]='.'
                    row[r]=0
                    lowerdiagonal[r+col]=0
                    upperdiagonal[n-1+(col-r)]=0
        chess=[['.' for i in range(n)] for j in range(n)]
        row = [0 for i in range(n)]
        lowerdiagonal= [0 for i in range(2*n-1)]
        upperdiagonal = [0 for i in range(2*n-1)]
        result=[]
        solve(chess,row,lowerdiagonal,upperdiagonal,result,0)
        return result
