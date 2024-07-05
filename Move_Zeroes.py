class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for index in range(0,len(nums)):
            if(nums[index]!=0):
                nums[non_zero],nums[index]=nums[index],nums[non_zero]
                non_zero+=1
