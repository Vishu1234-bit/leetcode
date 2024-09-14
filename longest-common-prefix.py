class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==1):
            return strs[0]
        index=0
        maxPrefix = ""
        while(index<len(strs)-1):
            common = ""
            if(index==0):
                string1 = strs[index]
            else:
                string1 = maxPrefix
            string2 = strs[index+1]
            traverseLen = min(len(string1),len(string2))
            strIndex = 0
            while(strIndex<traverseLen):
                if(string1[strIndex]==string2[strIndex]):
                    common+=string2[strIndex]
                else:
                    break
                strIndex+=1
            maxPrefix = common
            index+=1
        return maxPrefix
