class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1
        left = 0 
        right = len(matrix[0])-1
        result = []
        while(top<=bottom and left<=right):
            #top row
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            #right col
            for j in range(top,bottom+1):
                result.append(matrix[j][right])
            right-=1
            #bottom row
            if(top<=bottom):
                for k in range(right,left-1,-1):
                    result.append(matrix[bottom][k])
                bottom-=1
            #left col
            if(left<=right):
                for l in range(bottom,top-1,-1):
                    result.append(matrix[l][left])
                left+=1
        return result




        
