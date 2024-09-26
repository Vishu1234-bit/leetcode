class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if(len(nums)<=4):
            return 0
        else:
            n=len(nums)-1
            nums.sort()
            minDiff = nums[-1]-nums[0]
            for i in range(0,4):
                minDiff = min(minDiff,nums[(n-3)+i]-nums[i])
            return minDiff
        
