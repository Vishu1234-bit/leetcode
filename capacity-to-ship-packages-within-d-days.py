class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDays(mid):
            n=len(weights)
            load=0
            days=1
            for i in range(n):
                if(load+weights[i]>mid):
                    days+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            return days
        low = max(weights)
        high = sum(weights)
        while(low<=high):
            mid=(low+high)//2
            if(getDays(mid)<=days):
                high=mid-1
            else:
                low=mid+1
        return low
        
