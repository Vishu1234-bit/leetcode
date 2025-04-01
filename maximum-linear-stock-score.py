class Solution:
    def maxScore(self, prices: List[int]) -> int:
        max_score=0
        dp = [0 for i in range(len(prices))]
        n = len(prices)
        bestdp={}
        for i in range(n):
            dp[i] =prices[i]
            if(i>0):
                key = prices[i]-i
                if(key in bestdp):
                    dp[i] = max(bestdp[key]+prices[i],dp[i])
            key=prices[i]-i
            max_score = max(dp[i],max_score)
            bestdp[key] = max(bestdp.get(key,0),dp[i])
        return max_score
        


