class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(not points or not len(points)):
            return 0
        rowLen,colLen = len(points),len(points[0])
        dp = points[0][:]
        print(dp[0])
        for i in range(1,rowLen):
            new_dp = [0]*colLen
            left = [0]*colLen
            left[0] = dp[0]
            for l in range(1,colLen):
                left[l] = max(left[l-1]-1,dp[l])
            right = [0]*colLen
            right[colLen-1] = dp[colLen-1]
            for r in range(colLen-2,-1,-1):
                right[r] = max(right[r+1]-1,dp[r]) 
            for k in range(colLen):
                new_dp[k] = max(left[k],right[k])+points[i][k]
            dp = new_dp
            print(dp)
        return max(dp)
