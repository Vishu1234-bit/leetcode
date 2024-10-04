class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        left=0
        right = len(s)-1
        temp=""
        ans=""
        while(left<=right and s[left]==" "):
            left+=1
        while(right>left and s[right]==" "):
            right-=1
        while(left<=right):
            if(s[left]!=" "):
                temp+=s[left]
                print(temp)
            elif(s[left]==" "):
                if(temp):
                    ans = temp+ " "+ans if ans else temp
                temp=""
            left+=1
        if(ans!=""):
            ans = temp+" "+ans
        else:
            ans=temp

        return ans
