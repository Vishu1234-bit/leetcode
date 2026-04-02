class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(permut):
            if(len(permut)==len(nums)):
                res.append(permut[:])
                return
            for num in nums:
                if(num in permut):
                    continue
                permut.append(num)
                backtrack(permut)
                permut.pop()
        res=[]
        backtrack([])
        return res
