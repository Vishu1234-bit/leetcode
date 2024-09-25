class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if(tuple(point) not in self.points):
            self.points[tuple(point)]=1
        else:
            self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        count=0
        x1,y1 = point
        for p in self.points:
            x2,y2 = p
            height = x2-x1
            width = y2-y1
            if(abs(height)!=abs(width) or x1==x2 or y1==y2):
                continue
            
            if((x1,y2) in self.points and (x2,y1) in self.points):
                count+=(self.points[(x2,y2)]*self.points[(x1,y2)]*self.points[(x2,y1)])
        return count




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
