class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestHistogram(arr):
            arr.append(0)
            stack = []
            maxarea =0
            for i in range(0,len(arr)):
                while stack and arr[stack[-1]]>arr[i]:
                    h = arr[stack.pop()]
                    w = i if not stack else i -stack[-1]-1
                    maxarea = max(maxarea,h*w)
                stack.append(i)
            return maxarea
        def prefixSum(arr):
            prefixSum=[[0 for i in range(len(arr[0]))]for j in range(len(arr))]
            for i in range(0,len(arr[0])):
                sumPrefix=0
                for j in range(0,len(arr)):
                    sumPrefix+=int(arr[j][i])
                    if(arr[j][i] == '0'):
                        sumPrefix=0
                    prefixSum[j][i] = sumPrefix
            return prefixSum
        maxarea=0
        prefixSumMatrix = prefixSum(matrix)
        for arr in prefixSumMatrix:
            maxarea = max(largestHistogram(arr),maxarea)
        return maxarea
        

                    
                    
        
        
