class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        indexWord1 = 0
        indexWord2 = 0
        result = ""
        while(indexWord1<len(word1) and indexWord2<len(word2)):
            result+=word1[indexWord1]
            result+=word2[indexWord2]
            indexWord1+=1
            indexWord2+=1
        while(indexWord1<len(word1)):
            result+=word1[indexWord1]
            indexWord1+=1
        while(indexWord2<len(word2)):
            result+=word2[indexWord2]
            indexWord2+=1
        return result
