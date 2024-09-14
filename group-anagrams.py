class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        resultArr = []
        for anagram in strs:
            frequency = [0]*26
            for char in anagram:
                frequency[ord(char)-ord('a')]+=1
            frequency = tuple(frequency)
            if(frequency not in anagramDict):
                anagramDict[frequency] = [anagram]
            else:
                anagramDict[frequency].append(anagram)
        for i in anagramDict:
            resultArr.append(anagramDict[i])
        return resultArr
        

        
