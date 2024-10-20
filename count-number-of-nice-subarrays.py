class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        odd=0
        left=0
        right=0
        countsub=0
        while(right<len(nums)):
            if(nums[right]%2!=0):
                odd+=1
                countsub=0
            while(odd==k):
                if(nums[left]%2!=0):
                    odd-=1
                left+=1
                countsub+=1
            result+=countsub
            right+=1
        
        return result            
