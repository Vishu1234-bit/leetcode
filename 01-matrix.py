class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque([])
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    queue.append((i,j))
                else:
                    mat[i][j]=-1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while(queue):
            curr_r ,curr_c =queue.popleft()
            for drow,dcol in directions:
                newr , newc = curr_r+drow,curr_c+dcol
                if(0<=newr<m and 0<=newc<n and mat[newr][newc]==-1):
                    mat[newr][newc] = mat[curr_r][curr_c]+1
                    queue.append((newr,newc))
        return mat
                        
                
                    
