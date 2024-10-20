class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        abcdict={'a':0,'b':0,'c':0}
        left=0
        right=0
        result=0
        while(right<len(s)):
            if(s[right] in abcdict):
                abcdict[s[right]]+=1
            while(abcdict['a']>0 and abcdict['b']>0 and abcdict['c']>0):
                result+=(len(s)-right)
                if(s[left] in abcdict):
                    abcdict[s[left]]-=1
                left+=1
            right+=1
        return result
