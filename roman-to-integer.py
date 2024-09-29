class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000}
        index=0
        result=0
        while(index<len(s)):
            if(s[index:index+2] in romans):
                result+=romans[s[index:index+2]] 
                index+=2
            else:
                result+=romans[s[index]]
                index+=1 
        return result      
