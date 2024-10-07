class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calculateBeauty(frequency):
            max_freq = max([count for count in frequency if count>0])
            min_freq = min([count for count in frequency if count>0])
            return max_freq-min_freq
        total=0
        for i in range(len(s)):
            frequency=[0]*26
            for j in range(i,len(s)):
                frequency[ord(s[j])-ord('a')]+=1
                total+=calculateBeauty(frequency)
        return total
