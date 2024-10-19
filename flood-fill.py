class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if(image[sr][sc]==color):
            return image
        else:
            startColor = image[sr][sc]
            m = len(image)
            n = len(image[0])
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            queue = deque([(sr,sc)])
            image[sr][sc] = color
            while(queue):
                row,col = queue.popleft()
                for drow,dcol in directions:
                    newrow,newcol = row+drow,col+dcol
                    if(0<=newrow<m and 0<=newcol<n and image[newrow][newcol]==startColor):
                        image[newrow][newcol] = color
                        queue.append((newrow,newcol))
            return image

            
