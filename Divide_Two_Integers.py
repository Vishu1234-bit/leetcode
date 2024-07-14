class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if((dividend>=0 and divisor<0) or (dividend<0 and divisor>=0)):
            sign = -1 
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if(divisor == 1):
            result = dividend
        else:
            result = len(range(0,dividend-divisor+1,divisor))
        if(sign == -1):
            result  = -result
        minusLimit = -(2**31)
        plusLimit = 2**31-1
        if(result>plusLimit):
            return plusLimit
        elif(result<minusLimit):
            return minusLimit
        return result
        
