class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        bisect.insort(self.intervals,[left,right])
        res = [self.intervals[0]]
        for interval in self.intervals:
            if(res[-1][1]>=interval[0]):
                res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)
        self.intervals = res
    def queryRange(self, left: int, right: int) -> bool:
        index = bisect.bisect(self.intervals,[left,int(1e9)])
        if(not self.intervals or index==0):
            return False
        return self.intervals[index-1][1]>=right 
    def removeRange(self, left: int, right: int) -> None:
        res = []  
        for interval in self.intervals:
            if(interval[1]<=left or interval[0]>=right):
                res.append(interval)
            else:
                if(interval[0]<left):
                    res.append([interval[0],left])
                if(interval[1]>right):
                    res.append([right,interval[1]])

        self.intervals=res


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
