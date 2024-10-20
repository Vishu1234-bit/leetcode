class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
                
        left=0
        right=0
        minlen = float('inf')
        minsubsequence=""
        n = len(s1)
        m = len(s2)
        i=0
        while(i<n):
            j=0
            while(i<n):
                if(s2[j]==s1[i]):
                    j+=1
                if(j==m):
                    break
                i+=1
            if(j!=m):
                break
            end=i
            j=m-1
            while(j>=0):
                if(s1[i]==s2[j]):
                    j-=1
                i-=1
            i+=1
            if(end-i+1<minlen):
                minlen=end-i+1
                minsubsequence=s1[i:end+1]
            i=i+1
        return minsubsequence
            
                
