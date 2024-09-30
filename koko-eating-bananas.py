import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateTotalHours(m):
            th=0
            for noOfBanana in piles:
                th+=math.ceil(noOfBanana/m)
            return th
        maxBananas = max(piles)
        low = 1
        high = maxBananas
        while(low<=high):
            mid = (low+high)//2
            if(calculateTotalHours(mid)>h):
                low = mid+1
            else:
                high = mid-1
        return low
        
