class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left=0
        right=0
        minlen = float('inf')
        minsubstring = ""
        frequency = defaultdict(int)
        tfreq = Counter(t)
        formed=0
        required = len(tfreq)
        while(right<len(s)):
            char = s[right]
            frequency[char]+=1
            if(char in tfreq and tfreq[char]==frequency[char]):
                formed+=1
            while(left<=right and formed==required):
                char=s[left]
                if(minlen > right-left+1):
                    minlen = right-left+1
                    minsubstring = s[left:right+1]
                frequency[char]-=1
                if(char in tfreq and frequency[char]<tfreq[char]):
                    formed-=1
                left+=1
            right+=1
        return minsubstring if(minlen!=float('inf')) else ""
