class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        countPoints=0
        n = len(cardPoints)
        for idx in range(len(cardPoints)):
            countPoints+=cardPoints[idx]
        if(k==n):
            return countPoints
        minwindowsum = sum(cardPoints[:n-k])
        currentsum = minwindowsum
        for i in range(n-k,n):
            currentsum+=cardPoints[i]-cardPoints[i-(n-k)]
            minwindowsum = min(minwindowsum,currentsum)
        result = countPoints-minwindowsum
        return result
