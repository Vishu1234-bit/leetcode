class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        elif(n==1):
            return nums[0]
        elif(n==2):
            return max(nums[0],nums[1])
        else:
            dp=[]
            dp.append(nums[0])
            dp.append(max(nums[0],nums[1]))
            print(dp)
            for i in range(2,n):
                dp.append(max(dp[i-2]+nums[i],dp[i-1]))
                print(dp)
            return dp[n-1]


        
