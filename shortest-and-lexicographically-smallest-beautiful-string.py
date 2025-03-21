class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        countOf1 = 0
        shortlength=float('inf')
        shortsubstring=''
        for right in range(len(s)):
            if(s[right]=='1'):
                countOf1+=1
                print(countOf1)
            while(countOf1>k or (countOf1==k and s[left]=='0')):
                if(s[left]=='1'):
                    countOf1-=1
                left+=1
                print(countOf1,left)
            if(countOf1==k):
                if(right-left+1<shortlength):
                    shortsubstring = s[left:right+1]
                    shortlength=right-left+1
                elif(right-left+1==shortlength and s[left:right+1]<shortsubstring):
                    shortsubstring = s[left:right+1]
                print(shortsubstring,shortlength)
        return shortsubstring

            


        
