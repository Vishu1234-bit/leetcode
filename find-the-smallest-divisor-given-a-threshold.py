import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isSmallestDivisor(m):
            result=0
            for i in nums:
                result+=math.ceil(i/m)
            return result
        n=len(nums)
        if(n>threshold):
            return -1
        low=1
        high = max(nums)
        while(low<=high):
            mid=(low+high)//2
            if(isSmallestDivisor(mid)<=threshold):
                high = mid-1
            else:
                low=mid+1
        return low

        
