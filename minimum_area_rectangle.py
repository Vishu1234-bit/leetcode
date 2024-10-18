class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        minarea=float('inf')
        xcoords = {}
        for i in points:
            x,y = i
            if(x not in xcoords):
                xcoords[x]=[]
            xcoords[x].append(y)
        lastx={}
        for x in sorted(xcoords.keys()):
            ylist = xcoords[x]
            ylist.sort()
            for i in range(len(ylist)):
                for j in range(i+1,len(ylist)):
                    y1,y2=ylist[i],ylist[j]
                    if((y1,y2) in lastx):
                        width = x-lastx[(y1,y2)]
                        height = abs(y1-y2)
                        minarea = min(minarea,height*width)
                    lastx[(y1,y2)]=x
        return minarea if minarea!=float('inf') else 0
