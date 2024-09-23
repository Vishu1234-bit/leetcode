class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        power=1
        n_mod=abs(n)
        while(n_mod>0):
            if(n_mod%2):
                power*=x
            x*=x
            n_mod//=2
        if(n>0):
            return power
        else:
            return 1/power
        
