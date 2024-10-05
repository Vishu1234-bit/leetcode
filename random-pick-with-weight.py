import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w=w
        self.cumulativeWeights = []
        totsum=0
        for i in self.w:
            totsum+=i
            self.cumulativeWeights.append(totsum)

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1,self.cumulativeWeights[-1])
        low,high = 0,len(self.cumulativeWeights)
        while(low<high):
            mid = (low+high)//2
            if(target>self.cumulativeWeights[mid]):
                low=mid+1
            else:
                high = mid
        return low

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
