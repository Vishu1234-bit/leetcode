class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefixSum={0:1}
        countsum=0
        result=0
        for num in nums:
            countsum+=num
            if(countsum-goal in prefixSum):
                result+=(prefixSum[countsum-goal])
            if(countsum in prefixSum):
                prefixSum[countsum]+=1
            else:
                prefixSum[countsum]=1
        return result
