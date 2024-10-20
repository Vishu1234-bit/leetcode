class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        frequency = defaultdict(int)
        left=0
        right=0
        maxlen=0
        while(right<len(s)):
            frequency[s[right]]+=1
            while(len(frequency)>k):
                if(s[left] in frequency):
                    frequency[s[left]]-=1
                if(frequency[s[left]]==0):
                    del frequency[s[left]]
                left+=1
            if(right-left+1>maxlen):
                maxlen = right-left+1
            right+=1
        return maxlen

        
