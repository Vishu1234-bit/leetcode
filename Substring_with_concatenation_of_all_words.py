class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if(not words):
            return []
        dict={}
        wordsdict ={}
        for i in words:
            if(i not in wordsdict):
                wordsdict[i]=1
            else:
                wordsdict[i]+=1
        output=[]
        substr_len = len(words)*len(words[0])
        word_len = len(words[0])
        for i in range(0,len(s)-substr_len+1):
            seendict = {}
            for j in range(i,i+substr_len,word_len):
                word = s[j:j+word_len]
                if(word in wordsdict):
                    if(word not in seendict):
                        seendict[word]=1
                    else:
                        seendict[word]+=1
                    if(seendict[word]>wordsdict[word]):
                        break
                else:
                    break
            else:
                output.append(i)
        return output
