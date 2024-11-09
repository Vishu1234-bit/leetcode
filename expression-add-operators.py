class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def recursion(currentVal,prevOperand,index,expression):
            if(index==len(num)):
                if(currentVal==target):
                    res.append(expression)
                return
            for i in range(index,len(num)):
                if(i!=index and num[index]=='0'):
                    break
                curr_str = num[index:i+1]
                curr_num = int(curr_str)
                if(index==0):
                    recursion(curr_num,curr_num,i+1,curr_str)
                else:
                    recursion(currentVal+curr_num,curr_num,i+1,expression+"+"+curr_str)
                    recursion(currentVal-curr_num,-curr_num,i+1,expression+"-"+curr_str)
                    recursion(currentVal-prevOperand+(prevOperand*curr_num),prevOperand*curr_num,i+1,expression+"*"+curr_str)
                    

        res=[]
        recursion(0,0,0,'')
        return res
        
