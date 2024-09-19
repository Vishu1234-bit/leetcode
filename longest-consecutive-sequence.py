class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        numsSet = set()
        maxLen = 0
        count=1
        for i in nums:
            numsSet.add(i)
        for num in numsSet:
            if(num-1  not in numsSet):
                currentNum = num
                count =1
                while(currentNum+1 in numsSet):
                    currentNum+=1
                    count+=1
            maxLen = max(count,maxLen)
        return maxLen

