class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        numsBurst = [1]+nums+[1]
        dp = {}
        def dfs(l,r):
            if(l>r):
                return 0
            if((l,r) in dp):
                return dp[(l,r)]
            dp[(l,r)]=0       
            for i in range(l,r+1):
                coins = numsBurst[l-1]*numsBurst[i]*numsBurst[r+1]
                coins+=(dfs(l,i-1)+dfs(i+1,r))  
                dp[(l,r)]= max(coins,dp[(l,r)])
            return dp[(l,r)]
        return dfs(1,len(numsBurst)-2)
        

        
