class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]<nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
        diff = 20001
        value=0
        for i in range(len(nums)):
            a=i+1
            n=len(nums)-1
            while(a<n):
                sum=nums[i]+nums[a]+nums[n]
                actual_diff = abs(sum-target)
                if(actual_diff<diff):
                    diff = actual_diff
                    value = sum
                if(sum==target):
                    return target
                elif(sum<target):
                    a+=1
                else:
                    n-=1
        return value
