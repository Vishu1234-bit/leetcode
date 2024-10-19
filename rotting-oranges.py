class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        freshOranges=0
        queue = deque([])
        minutesPassed=0
        for r in range(m):
            for c in range(n):
                if(grid[r][c]==2):
                    queue.append((r,c,0))
                elif(grid[r][c]==1):
                    freshOranges+=1
        if(freshOranges==0):
            return 0
        while(queue):
            row,col,minutes = queue.popleft()
            minutesPassed=minutes
            for drow,dcol in directions:
                newrow,newcol = row+drow,col+dcol
                if(0<=newrow<m and 0<=newcol<n and grid[newrow][newcol]==1):
                    grid[newrow][newcol]=2
                    freshOranges-=1
                    queue.append((newrow,newcol,minutes+1))
        if(freshOranges>0):
            return -1
        return minutesPassed
       
        
