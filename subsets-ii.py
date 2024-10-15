class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=set()
        def backtrack(start,subset):
            if(start==len(nums)):
                result.add(tuple(sorted(subset[:])))
                return
            result.add(tuple(sorted(subset[:])))
            for i in range(start,len(nums)):
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return result
