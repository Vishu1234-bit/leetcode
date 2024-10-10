class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first=0
        last = len(height)-1
        maxWater = 0
        while(first<=last):
            h = min(height[first],height[last])
            w = last-first
            maxWater = max(h*w,maxWater)
            if(height[first]<height[last]):
                first+=1
            else:
                last-=1
        return maxWater
            
