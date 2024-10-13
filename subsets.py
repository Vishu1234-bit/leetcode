class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(idx,subset):
            if(idx>=len(nums)):
                res.append(subset[:])
                return
            backtrack(idx+1,subset)
            subset.append(nums[idx])
            backtrack(idx+1,subset)
            subset.pop()
        res=[]
        backtrack(0,[])
        return res
