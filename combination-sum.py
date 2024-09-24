class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        combination = deque()
        def backtrack(sumtillindex,start):
            if(sumtillindex==target):
                res.add(tuple(sorted(combination)))
                return
            elif(sumtillindex>target):
                return
            else:
                for i in range(start,len(candidates)):
                    combination.append(candidates[i])
                    backtrack(sumtillindex+candidates[i],start)
                    combination.pop()
        backtrack(0,0)
        return res
