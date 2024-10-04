class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==1):
            return strs[0]
        prefix = strs[0]
        for i in range(1,len(strs)):
            word2 = strs[i]
            index=0
            while(index<len(prefix) and index<len(word2)):
                if(prefix[index] != word2[index]):
                    break
                index+=1
            prefix = prefix[:index]
            if(not prefix):
                return ""
        return prefix
            

        
