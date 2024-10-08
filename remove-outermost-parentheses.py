class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        balance=0
        result=[]
        for i in range(len(s)):
            if(s[i]=='('):
                if(balance>0):
                    result.append(s[i])
                balance+=1
            else:
                balance-=1
                if(balance>0):
                    result.append(s[i])
        return ''.join(result)
