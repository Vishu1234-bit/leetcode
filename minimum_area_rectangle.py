class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set(map(tuple,points))
        min_Area = float('inf')
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                x1,y1 = points[i][0],points[i][1]
                x2,y2 = points[j][0],points[j][1]
                if((x1!=x2 and y1!=y2)):
                    if((x1,y2) in points_set and (x2,y1) in points_set):
                        area = abs(x1-x2)*abs(y1-y2)
                        min_Area = min(area,min_Area)
        if(min_Area!=float('inf')):
            return min_Area
        else:
            return 0      

        
