class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        numCopy = int(num)
        ans=-1
        while(numCopy>0):
            if(numCopy%2==0):
                numCopy//=10
            else:
                ans= numCopy
                break
        return str(ans) if(ans>0) else ""
