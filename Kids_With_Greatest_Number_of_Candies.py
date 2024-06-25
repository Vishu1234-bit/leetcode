class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        def isMax(i,arr):
            for j in arr:
                if(i<j):
                    return False
            return True
        greater_candy = [False]*len(candies)
        for i in range(0,len(candies)):
            if(isMax(candies[i]+extraCandies,candies)):
                greater_candy[i] = True
        return greater_candy
