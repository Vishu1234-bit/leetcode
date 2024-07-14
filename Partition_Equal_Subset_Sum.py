class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        for i in nums:
            totalSum+=i
      
        if(totalSum%2==0):
            subsetArr = 0
            sumSet = set([0])
            for i in nums:
                tempset=set()
                for s in sumSet:
                    if(s+i == totalSum//2):
                        return True
                    tempset.add(s+i)
                sumSet.update(tempset)
        else:
            return False
