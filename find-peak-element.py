class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1 or nums[0]>nums[1]):
            return 0
        if(nums[-1]>nums[-2]):
            return n-1
        l=1
        r=n-2
        ans = -1
        while(l<=r):
            m=(l+r)//2
            if(nums[m]>nums[m-1] and nums[m]>nums[m+1]):
                ans=m
                return ans
            if(nums[m]>=nums[m-1]):
                l=m+1
            else:
                r = m-1
        return ans
