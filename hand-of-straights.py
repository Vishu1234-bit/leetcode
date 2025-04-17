class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize!=0):
            return False
        count = Counter(hand)
        sortedKeys = sorted(count.keys())
        for num in sortedKeys:
            if(count[num]>0):
                freq = count[num]
                for i in range(num,num+groupSize):
                    if(count[i]<freq):
                        return False
                    count[i]-=freq
        return True


                
                    
                    
                
