class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        n=len(nums)-1
        if(nums[0]!=nums[1]):
            return nums[0]
        if(nums[n]!=nums[n-1]):
            return nums[n] 
        l=1
        r=n-2
        while(l<=r):
            m=(l+r)//2    
            print(m)
            if(nums[m]!=nums[m-1] and nums[m]!=nums[m+1]):
                return nums[m]     
            if((m%2==0 and nums[m]==nums[m+1]) or (m%2==1 and nums[m]==nums[m-1])):
                l=m+1
                print("incrementing l")
            else:
                r=m-1
                print("incrementing r")
        
        
