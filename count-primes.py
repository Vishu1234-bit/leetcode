import math
class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            limit = int(math.sqrt(n))+1
            if(n<=1):
                return False
            if(n<=3):
                return True
            if(n%2==0 and n%3==0):

                return False
            for i in range(5,limit,6):
                if(n%i==0 or n%(i+2)==0):
                    return False
            return True
        if(n<2):
            return 0
        isPrimeArray = [True]*n
        isPrimeArray[0]=False
        isPrimeArray[1]=False
        limit = int(math.sqrt(n))+1
        for i in range(2,limit):
            if(isPrime(i)):
                for multiple in range(i*i,n,i):
                    isPrimeArray[multiple]=False
        return sum(isPrimeArray)


                
