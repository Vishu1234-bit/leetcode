class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for currency in bills:
            if(currency==5):
                five+=1
            elif(currency==10):
                if(five>0):
                    five-=1
                else:
                    return False
                ten+=1
            elif(currency==20):
                if(ten>0 and five>0):
                    ten-=1
                    five-=1
                elif(five>=3):
                    five-=3
                else:
                    return False
        return True
