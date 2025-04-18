class Solution:
    def myAtoi(self, s: str) -> int:
        result=0
        index=0
        sign =1
        charRead = False
        while(index<len(s)):
            if(s[index]=='-' and not charRead):
                sign=-1
                index+=1
                charRead=True
            elif(s[index]=='+' and not charRead):
                sign=1
                index+=1
                charRead = True
            elif(s[index].isdigit()):
                result=result*10+int(s[index])
                charRead=True
                index+=1
            elif((s[index]==' ' or s[index]=='0') and not charRead):
                index+=1
            else:
                break
        if(sign*result>=2**31):
            return (2**31)-1
        elif(sign*result<=(-2**31)):
            return -2**31
        return sign*result
