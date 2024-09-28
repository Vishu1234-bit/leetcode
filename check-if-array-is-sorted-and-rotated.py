class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        countbreaks=0
        for i in range(0,len(nums)):
            if(nums[i]>nums[(i+1)%n]):
                countbreaks+=1
            if(countbreaks>1):
                return False
        return True
