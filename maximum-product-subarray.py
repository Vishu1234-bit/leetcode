class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        maxProduct=float('-inf')
        for i in range(0,len(nums)):
            if(prefix==0):
                prefix=1
            if(suffix==0):
                suffix=1
            prefix*=nums[i]
            suffix*=nums[len(nums)-i-1]
            maxProduct = max(maxProduct,max(prefix,suffix))
        return maxProduct
