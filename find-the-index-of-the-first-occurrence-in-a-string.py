class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle not in haystack):
            return -1
        else:
            ans=-1
            for i in range(0,len(haystack)):
                if(haystack[i]==needle[0]):
                    print(i)
                    startIndex = i
                    needleStart=0
                    while(startIndex<len(haystack) and needleStart<len(needle) and haystack[startIndex]==needle[needleStart]):
                        needleStart+=1
                        startIndex+=1
                    if(needleStart==len(needle)):
                        ans=i
                        break
            return ans
                

        
