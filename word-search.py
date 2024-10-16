class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(row,col,index):
            if(index==len(word)):
                return True
            if(row<0 or col<0 or row>=len(board) or col>=len(board[0]) or board[row][col]!=word[index]):
                return False
            temp = board[row][col]
            board[row][col]="#"
            found = (dfs(row+1,col,index+1) or
            dfs(row-1,col,index+1) or
            dfs(row,col+1,index+1) or
            dfs(row,col-1,index+1) )
            board[row][col]=temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0]):
                    if(dfs(i,j,0)):
                        return True
        return False
