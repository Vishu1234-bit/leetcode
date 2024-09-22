class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            return s[left+1:right]
        maxlen = float('-inf')
        substring=""
        palindromeeven = ""
        for i in range(len(s)):
            palindromeodd = expandAroundCenter(i,i)
            if(i+1<len(s)):
                palindromeeven = expandAroundCenter(i,i+1)
            if(len(palindromeodd)>maxlen):
                maxlen = len(palindromeodd)
                substring = palindromeodd
            if(len(palindromeeven)>maxlen):
                maxlen = len(palindromeeven)
                substring = palindromeeven
            

        return substring

        
