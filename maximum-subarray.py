class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumSubArr =0 
        maxSum = float('-inf')
        for i in range(0,len(nums)):
            sumSubArr+=nums[i]
            if(sumSubArr>maxSum):
                maxSum = sumSubArr
            if(sumSubArr<0):
                sumSubArr = 0
        return maxSum

            
        
