class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=3
        m=301
        dp={}
        for i,ele in enumerate(nums):
            best=1
            for diff in range(m-1,-1,-1):
                if(ele+diff<m):
                    if((ele+diff,diff) in dp):
                        best = max(best,dp[(ele+diff,diff)]+1)
                if(ele-diff>=0):
                    if((ele-diff,diff) in dp):
                        best = max(best,dp[(ele-diff,diff)]+1)
                dp[ele,diff]=best
        return max(dp.values())
