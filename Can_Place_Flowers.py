class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        if(n==0):
            return True
        if(len(flowerbed)==1):
            if(flowerbed[0] == 0 and n==1):
                return True
            elif(flowerbed[0]==1 and n==0):
                return True
            else:
                return False
        if(len(flowerbed)>2 and flowerbed[0]==0 and flowerbed[1]==0):
            placed+=1
            flowerbed[0]=1
        if(placed==n):
            return True
        for i in range(1,len(flowerbed)-1):
            if(flowerbed[i]==0):
                if(flowerbed[i-1]==1):
                    continue
                else:
                    if(flowerbed[i+1]==1):
                        continue
                    else:
                        placed+=1
                        flowerbed[i]=1
                if(placed==n):
                    return True
        if(flowerbed[-1]==0 and flowerbed[-2]==0):
            placed+=1
            flowerbed[-1]=1
        if(placed==n):
            return True
        return False     
