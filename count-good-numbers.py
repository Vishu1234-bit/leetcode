class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod= 10**9+7
        def myPow(n,x):
            if(n==0):
                return 1
            if(n<0):
                x=1/x
                n=-n
            if(n%2==0):
                half = myPow(n//2,x)
                return (half*half)%mod
            else:
                return (x*myPow(n-1,x))%mod
        if(n==1):
            return 5
        if(n%2!=0):
            return (myPow((n+1)//2,5)*myPow(n//2,4))%mod
        else:
            return (myPow(n//2,5)*myPow(n//2,4))%mod
