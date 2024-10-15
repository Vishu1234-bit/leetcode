class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(start,combination):
            if(len(combination)==k and sum(combination)==n):
                result.append(combination[:])
                return
            for i in range(start,10):
                combination.append(i)
                print(combination)
                backtrack(i+1,combination)
                combination.pop()
        backtrack(1,[])
        return result
