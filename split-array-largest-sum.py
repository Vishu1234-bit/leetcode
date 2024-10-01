class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countPartitions(maxsum):
            n = len(nums)
            subArraySum = 0
            partitions = 1
            for i in range(n):
                if(subArraySum+nums[i]<=maxsum):
                    subArraySum+=nums[i]
                else:
                    partitions+=1
                    subArraySum=nums[i]
            return partitions
        low=max(nums)
        high = sum(nums)
        while(low<=high):
            mid = (low+high)//2
            partition = countPartitions(mid)
            if(partition>k):
                low = mid+1
            else:
                high = mid-1
        return low

        
