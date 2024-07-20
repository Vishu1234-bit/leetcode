class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start,combinations):
            if(len(combinations)==k):
                result.append(combinations[:])
                return 
            for i in range(start,n+1):
                combinations.append(i)
                backtrack(i+1,combinations)
                combinations.pop()
        backtrack(1,[])
        return result
