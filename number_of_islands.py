class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(not grid):
            return 0
        rowlen,collen = len(grid),len(grid[0])
        def dfs(row,col):
            if(row>=rowlen or col>=collen or row<0 or col<0 or grid[row][col]=="0"):
                return
            grid[row][col]='0'
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        islandCount=0
        for i in range(rowlen):
            for j in range(collen):
                if(grid[i][j]=="1"):
                    dfs(i,j)
                    islandCount+=1
        return islandCount
       
