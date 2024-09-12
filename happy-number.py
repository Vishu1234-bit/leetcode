class Solution:
    def isHappy(self, n: int) -> bool:
        def computeSquaresOfDigits(num):
            sum=0
            while(num>0):
                rem = num%10
                sum+=(rem*rem)
                num = num//10
            return sum
        numsEncountered = []
        while(True):
            next_n =computeSquaresOfDigits(n) 
            if(next_n==1):
                return True
            if(next_n in numsEncountered):
                return False
            numsEncountered.append(next_n)
            n = next_n


        
