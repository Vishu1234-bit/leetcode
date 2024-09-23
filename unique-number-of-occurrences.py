class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if(i in hashmap):
                hashmap[i]+=1
            else:
                hashmap[i]=1
        occurence = []
        for i in hashmap:
            if(hashmap[i] in occurence):
                return False
            occurence.append(hashmap[i])
        return True

        
