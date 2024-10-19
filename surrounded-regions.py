class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def bfs(i,j):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            queue=deque([(i,j)])
            board[i][j] ='T'
            while(queue):
                currr,currc = queue.popleft()
                for dr,dc in directions:
                    newr,newc = currr+dr,currc+dc
                    if(0<=newr<m and 0<=newc<n and board[newr][newc]=='O'):
                        board[newr][newc] = 'T'
                        queue.append((newr,newc))
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if(board[i][0]=='O'):
                bfs(i,0)
            if(board[i][n-1]=='O'):
                bfs(i,n-1)
        for j in range(n):
            if(board[0][j]=='O'):
                bfs(0,j)
            if(board[m-1][j]=='O'):
                bfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if(board[i][j]=='T'):
                    board[i][j]='O'
                elif(board[i][j]=='O'):
                    board[i][j]='X'
        return board
