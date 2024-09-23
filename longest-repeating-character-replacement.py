class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = [0 for i in range(0,26)]
        maxlen = 0
        maxfreq = 0
        left=0
        right=0
        while(right<len(s)):
            frequency[ord(s[right])-ord('A')]+=1
            print(frequency)
            maxfreq = max(maxfreq,frequency[ord(s[right])-ord('A')])
            print(maxfreq,maxlen)
            while((right-left+1)-maxfreq>k):
                frequency[ord(s[left])-ord('A')]-=1
                left+=1
                maxfreq = max(maxfreq,frequency[ord(s[left])-ord('A')])
            maxlen = max(maxlen,right-left+1)
            right+=1
        return maxlen
        

        
