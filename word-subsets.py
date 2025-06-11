class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def mergeFrequencies(words2):
            requiredfreq = defaultdict(int)
            for word in words2:
                freq = Counter(word)
                for char in freq:
                    requiredfreq[char] = max(freq[char],requiredfreq[char])
            return requiredfreq
        requiredfrequencies = mergeFrequencies(words2)
        result=[]
        for word in words1:
            actualfrequency = Counter(word)
            if(all(actualfrequency[char]>=requiredfrequencies[char] for char in requiredfrequencies)):
                result.append(word)
        return result
