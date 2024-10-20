class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        right=0
        maxfreq = 0
        maxlen=0
        countOf1 = 0
        while(right<len(nums)):
            if(nums[right]==1):
                countOf1 +=1
            while(((right-left+1)-countOf1)>k):
                if(nums[left]==1):
                    countOf1-=1
                left+=1
            if((right-left+1)>maxlen):
                maxlen = right-left+1
            right+=1
        return maxlen
