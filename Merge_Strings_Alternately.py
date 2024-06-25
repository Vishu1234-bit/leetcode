class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1len = len(word1)
        word2len = len(word2)
        minlen = min(word1len,word2len)
        output_String = ""
        for i in range(0,minlen):
            output_String+=word1[i]
            output_String+=word2[i]
        if(word2len>minlen):
            for i in range(minlen,word2len):
                output_String+=word2[i]
        if(word1len>minlen):
            for i in range(minlen,word1len):
                output_String+=word1[i]       
        return output_String
