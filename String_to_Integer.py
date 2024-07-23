class Solution:
    def myAtoi(self, s: str) -> int:
        resultingS = ""
        for i in s:
            if(i.isdigit() or (i == '+' and resultingS=="") or (i=='-'and resultingS=="")):
                resultingS+=i
            elif(i == ' ' and resultingS==""):
                continue
            elif((i.isalpha() and resultingS=="")):
                return 0
            elif((i.isalpha() and resultingS!="") or (i=="+" and resultingS!="") or (i=="-" and resultingS!="") or (i==' ' and resultingS!="") or i=='.'):
                break
        if(resultingS!='' and resultingS!='+' and resultingS!='-'):
            if(int(resultingS)>2**31-1):
                return 2**31-1
            elif(int(resultingS)<(-2**31)):
                return -2**31
            else:
                return int(resultingS)
        else:
            return 0
