class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        def findMaxElement(arr,mid,n,m):
            maxi = float('-inf')
            index=-1
            for i in range(0,n):
                if(arr[i][mid]>maxi):
                    maxi = arr[i][mid]
                    index=i
            return index
        low = 0
        high = len(mat[0])-1
        n=len(mat)
        m=len(mat[0])
        print(n,m)
        while(low<=high):
            mid = (low+high)//2
            row = findMaxElement(mat,mid,n,m)
            left = mat[row][mid-1] if (mid-1)>=0 else -1
            right = mat[row][mid+1] if(mid+1)<m else -1
            print(left,right)
            if(mat[row][mid]>left and mat[row][mid]>right):
                return (row,mid)
            elif(left>mat[row][mid]):
                high=mid-1
            else:
                low=mid+1
        return (-1,-1)
