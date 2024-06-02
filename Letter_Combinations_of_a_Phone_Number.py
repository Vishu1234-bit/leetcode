class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        if not digits:
            return []
        telephone={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(index,path):
            if(index==len(digits)):
                res.append("".join(path))
                return
            for char in telephone[digits[index]]:
                path.append(char)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return res
            
