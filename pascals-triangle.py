class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        baseCase = [1]
        triangle = []
        for i in range(0,numRows):
            print(i)
            if(i==0):
                triangle.append(baseCase)
            else:
                row = [0 for i in range(i+1)] 
                row[0],row[-1] = 1,1
                for j in range(1,len(row)-1):
                    row[j] = triangle[-1][j-1]+triangle[-1][j]
                triangle.append(row)
        return triangle

        
