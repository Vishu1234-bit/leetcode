class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open,close,output):
            if(len(output)==n*2):
                res.append(output[:])
                return
            if(open<n):
                backtrack(open+1,close,output+'(')
            if(close<open):
                backtrack(open,close+1,output+')')
        res = []
        backtrack(0,0,"")
        return res
