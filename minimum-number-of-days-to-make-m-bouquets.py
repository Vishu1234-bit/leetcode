class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def formBouquet(days):
            flower=0
            noOfBouquetsFormed = 0
            for bloom in bloomDay:
                if(bloom<=days):
                    flower+=1
                    if(flower==k):
                        noOfBouquetsFormed+=1
                        flower=0
                else:
                    flower=0
            return noOfBouquetsFormed>=m
        if(m*k>len(bloomDay)):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while(low<high):
            mid = (low+high)//2
            if(formBouquet(mid)):
                high=mid
            else:
                low = mid+1
        return low
