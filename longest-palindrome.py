class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        for i in s:
            if(i not in hashmap):
                hashmap[i]=1
            else:
                hashmap[i]+=1
        length=0
        onechar=False
        for i in hashmap.values():
            if(i%2==0):
                length+=i
            else:
                length+=(i-1)
                onechar=True
        return length+1 if onechar else length
