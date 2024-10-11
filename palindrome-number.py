class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0 or (x%10==0 and x!=0)):
            return False
        reverse=0
        original = x
        while(x>0):
            reverse=reverse*10+(x%10)
            x//=10
        print(reverse)
        return reverse==original
        
