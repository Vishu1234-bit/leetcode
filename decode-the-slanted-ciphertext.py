class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if(rows==1):
            return encodedText
        cols = len(encodedText)//rows
        matrix = [encodedText[i*cols:(i+1)*cols] for i in range(rows)]
        result=[]
        for start_col in range(cols):
            i=0
            j=start_col
            while(i<rows and j<cols):
                result.append(matrix[i][j])
                i+=1
                j+=1
        return ''.join(result).rstrip()
