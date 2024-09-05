class MedianFinder:

    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        if(len(self.list)>=1):
            low,high=0,len(self.list) 
            while(low<high):  
                mid = (low+high)//2
                if(self.list[mid]<num):
                    low = mid+1
                else:
                    high =mid
            if(low>=0):
                self.list = self.list[:low]+[num]+self.list[low:]
            else:
                self.list.append(num)
        else:
            self.list.append(num)
    def findMedian(self) -> float:
        if(len(self.list)>=1):
            length = len(self.list)
            if(length%2==0):
                return ((self.list[length//2]+self.list[(length//2)-1])/2)
            else:
                return self.list[length//2]
    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
