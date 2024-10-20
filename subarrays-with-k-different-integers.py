class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmostK(k):
            left=0
            right=0
            frequency = defaultdict(int)
            result=0
            while(right<len(nums)):
                frequency[nums[right]]+=1
                while(len(frequency)>k):
                    if(nums[left] in frequency):
                        frequency[nums[left]]-=1
                    if(frequency[nums[left]]==0):
                        del frequency[nums[left]]
                    left+=1
                result+=right-left+1
                right+=1
            return result
        return atmostK(k)-atmostK(k-1)
