class Solution:
    def check(self, nums: List[int]) -> bool:
        original_nums = nums.copy()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]>nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
        if(nums==original_nums):
            return True
        rotations = 1
        while(rotations<len(original_nums)):
            if(nums[rotations:len(nums)]+nums[0:rotations] == original_nums):
                return True
            rotations+=1
        return False
