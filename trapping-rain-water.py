class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        water = 0
        leftmax = height[l]
        rightmax = height[r]
        while(l<r):
            if(leftmax<rightmax):
                l+=1
                leftmax = max(leftmax,height[l])
                water+=(leftmax-height[l])
            else:
                r-=1
                rightmax = max(rightmax,height[r])
                water+=(rightmax-height[r])
        return water

        
