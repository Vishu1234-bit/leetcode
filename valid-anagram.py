class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap={}
        for i in s:
            if(i not in smap):
                smap[i] = 1
            else:
                smap[i]+=1
        for i in t:
            if i not in smap:
                return False
            smap[i]-=1
            if(smap[i]==0):
                del smap[i]
        return len(smap)==0
