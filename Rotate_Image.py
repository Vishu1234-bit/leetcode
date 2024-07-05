class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] =matrix[j][i],matrix[i][j]
        for arr in matrix:
            left=0
            right=len(arr)-1
            while(left<=len(matrix)//2 and right>=len(matrix)//2):
                if(left!=right):
                    arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1 
