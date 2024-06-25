class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        present_vowels=[]
        for i in range(0,len(s)):
            if s[i] in vowels:
                present_vowels.append(s[i])
        place_vowels=-1
        list_s = list(s)
        for i in range(0,len(s)):
            if(s[i] in vowels):
                list_s[i]=present_vowels[place_vowels]
                place_vowels-=1
        

        return "".join(list_s)
