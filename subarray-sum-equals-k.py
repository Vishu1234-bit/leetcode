class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if(len(nums)==1 and k==nums[0]):
            return 1
        elif(len(nums)==1 and k!=nums[0]):
            return 0
        prefixSum = 0
        hashmap={}
        hashmap[prefixSum] = 1
        count=0
        for i in range(0,len(nums)):
            prefixSum+=nums[i]
            if(prefixSum-k in hashmap):
                count+=hashmap[prefixSum-k]
            if(prefixSum in hashmap):
                hashmap[prefixSum]+=1
            else:
                hashmap[prefixSum]=1
        return count


