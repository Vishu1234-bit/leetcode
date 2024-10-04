class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights.append(0)
        maxarea = 0
        for i in range(len(heights)):
            while(stack and heights[stack[-1]]>heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                maxarea = max(maxarea,h*w)
            stack.append(i)
        return maxarea
