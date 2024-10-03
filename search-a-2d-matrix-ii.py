class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(matrix[0])-1
        n = len(matrix)
        while(low<n and high>=0):
            if(matrix[low][high]==target):
                return True
            elif(matrix[low][high]>target):
                high-=1
            else:
                low+=1
        return False
