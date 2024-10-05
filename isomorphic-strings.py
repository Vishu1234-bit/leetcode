class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        indexs = [0]*200
        indext = [0]*200
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if(indexs[ord(s[i])]!=indext[ord(t[i])]):
                return False
            indexs[ord(s[i])]=i+1
            indext[ord(t[i])]=i+1 
        return True
