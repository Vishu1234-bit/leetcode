class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(substring):
            return substring[::-1]==substring
        result=[]
        def backtrack(start,palindromearr):
            if(start==len(s)):
                result.append(palindromearr[:])
                print(result)
                return 
               
            for i in range(start,len(s)):
                substring=s[start:i+1]
                if(isPalindrome(substring)):
                    palindromearr.append(substring)
                    backtrack(i+1,palindromearr)
                    print(palindromearr)
                    palindromearr.pop()
                    print(palindromearr)

        backtrack(0,[])
        return result
