class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_pointer=0
        t_pointer=0
        matched_index=[]
        while(s_pointer<len(s) and t_pointer<len(t)):
            if(s[s_pointer] == t[t_pointer]):
                matched_index.append(t_pointer)
                s_pointer+=1
                t_pointer+=1
            else:
                t_pointer+=1
        if(len(matched_index)==len(s)):
            return True
        else:
            return False
