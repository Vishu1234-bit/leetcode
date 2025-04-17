class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        childPointer = 0
        cookiePointer = 0 
        g.sort()
        s.sort()
        content=0
        while(childPointer<len(g) and cookiePointer<len(s)):
            if(g[childPointer] <= s[cookiePointer]):
                childPointer+=1
                cookiePointer+=1
                content+=1
            elif(g[childPointer] > s[cookiePointer]):
                cookiePointer+=1
            else:
                childPointer+=1
        return content



        
