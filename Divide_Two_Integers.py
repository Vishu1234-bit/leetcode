class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if((dividend>=0 and divisor<0) or (dividend<0 and divisor>=0)):
            sign = -1 
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if(divisor == 1):
            result = dividend
        else:
            result=0
            while(dividend>=divisor):
                temp,multiple=divisor,1
                print(temp,multiple,temp<<1)
                while(dividend>=(temp<<1)):
                    temp<<=1
                    multiple<<=1
                    print("after shifts",temp,multiple)
                dividend-=temp
                result+=multiple
                print(dividend,result)
                print(dividend,result)
        if(sign == -1):
            result  = -result
        minusLimit = -(2**31)
        plusLimit = 2**31-1
        if(result>plusLimit):
            return plusLimit
        elif(result<minusLimit):
            return minusLimit
        return result
        
