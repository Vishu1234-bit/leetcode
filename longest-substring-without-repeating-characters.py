class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countChars = {}
        index = 0 
        maxlength = 0
        startIndex = 0 
        endIndex = 0
        while(index<len(s)):
            if(s[index] not in countChars):
                countChars[s[index]]=index
            else:
                if(countChars[s[index]]+1>startIndex):
                    startIndex = countChars[s[index]]+1
                countChars[s[index]] = index
            endIndex = index
            if((endIndex-startIndex)+1>maxlength):
                    maxlength = (endIndex-startIndex)+1
            print(endIndex,startIndex,s[index],maxlength)
            index+=1
        return maxlength
        
