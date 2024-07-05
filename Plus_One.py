class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[-1]<9):
            digits[-1]+=1
        else:
            if(len(digits)==1 and digits[0]==9):
                digits = [1,0]
            else:
                digits[-1]=0
                index = len(digits)-2
                while(index>=0):
                    if(digits[index]==9 and index==0):
                        digits[index]=0
                        digits=[1]+digits
                        break
                    elif(digits[index]==9):
                        digits[index]=0
                    else:
                        digits[index]+=1
                        break
                    index-=1
        return digits        
