class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while(1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]):
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        for i in range(n):
            if(i+1!=nums[i]):
                return i+1
        return n+1
