class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=-1
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                k=i-1  
                break 
        if(k!=-1):
            j=-1
            for i in range(len(nums)-1,k,-1):
                if(nums[i]>nums[k]):
                    nums[i],nums[k]=nums[k],nums[i]
                    break
        first = k+1
        last  = len(nums)-1
        while(first<last):
            nums[first],nums[last] = nums[last],nums[first]
            first+=1
            last-=1         
