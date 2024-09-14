class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum = 0
        for i in nums:
            numsSum+=i
        rangeSum=0
        for j in range(0,len(nums)+1):
            rangeSum+=j
        return rangeSum-numsSum
        
