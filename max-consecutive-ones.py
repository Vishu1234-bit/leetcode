class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index =0 
        maxConsecutive = 0
        length=0
        while(index<len(nums)):
            if(nums[index]==1):
                length+=1
            else:
                length=0
            maxConsecutive = max(length,maxConsecutive)
            index+=1
        return maxConsecutive

        
