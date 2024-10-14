class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(candidates)
        combination = []
        def backtrack(sumtillindex,idx):
            if(sumtillindex==target):
                res.append(list(combination))
                return
            elif(sumtillindex>target):
                return
            else:
                for i in range(idx,len(candidates)):
                    if(i>idx and candidates[i]==candidates[i-1]):
                        continue
                    combination.append(candidates[i])
                    backtrack(sumtillindex+candidates[i],i+1)
                    combination.pop()
        backtrack(0,0)
        return res
