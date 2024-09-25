class Solution:
    def reverse(self, x: int) -> int:
        sign =1
        if(x<0):
            sign=-1
        num = abs(x)
        reverse = 0
        while(num>0):
            reverse = reverse*10+(num%10)
            num=num//10
        if((sign*reverse)<(-1*2**31) or (sign*reverse)>((2**31)-1)):
            return 0
        return sign*reverse

        
