class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        output = ""
        place = 1
        for n in range(0,len(numbers)):
            while(num>=numbers[n]):
                num-=numbers[n]
                output+=romans[n]
        return output
