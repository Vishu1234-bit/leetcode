class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def checkInRow(arr):
            low = 0
            high = len(arr)-1
            while(low<=high):
                mid = (low+high)//2
                if(arr[mid]==target):
                    return True
                elif(arr[mid]>target):
                    high = mid-1
                else:
                    low=mid+1
            return False
        low = 0
        high = len(matrix)-1
        while(low<=high):
            mid = (low+high)//2
            if(matrix[mid][0]>target):
                high = mid-1
            else:
                if(checkInRow(matrix[mid])):
                    return True
                else:
                    low = mid+1
        return False

        
