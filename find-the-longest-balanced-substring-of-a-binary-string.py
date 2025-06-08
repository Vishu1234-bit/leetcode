class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        groups=[]
        count=1
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                count+=1
            else:
                groups.append((count,s[i-1]))
                count=1
        groups.append((count,s[-1]))
        maxlen=0
        for i in range(1,len(groups)):
            if(groups[i-1][1]=='0' and groups[i][1]=='1'):
                maxlen = max(maxlen,2*min(groups[i-1][0],groups[i][0]))
        return maxlen
