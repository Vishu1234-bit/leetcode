class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        posIndex=0 
        negIndex=1
        for i in range(0,len(nums)):
            if(nums[i]<0):
                res[negIndex]=nums[i]
                negIndex+=2
            else:
                res[posIndex]=nums[i]
                posIndex+=2
        return res
