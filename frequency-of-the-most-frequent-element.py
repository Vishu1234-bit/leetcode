class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        left=0
        maxlength=0
        total=0
        for right in range(0,len(nums)):
            total+=nums[right]
            kneeded = ((right-left+1)*nums[right])-total
            while(kneeded>k and left<len(nums)):
                total-=nums[left]
                left+=1
                kneeded= ((right-left+1)*nums[right])-total
            maxlength = max(maxlength,right-left+1)
        return maxlength


        
