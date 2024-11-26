class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start^goal
        count=0
        while(res>0):
            count+=res&1
            res>>=1
        return count


        


        
