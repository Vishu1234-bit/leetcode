class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def findNSE(arr):
            nse=[0 for i in range(len(arr))]
            stack=[]
            for i in range(len(arr)-1,-1,-1):
                while(len(stack) and arr[stack[-1]]<=arr[i]):
                    stack.pop()
                if(len(stack)):
                    nse[i] = stack[-1]
                else:
                    nse[i] = len(arr)
                stack.append(i)
            return nse
        def findPSEE(arr):
            pse=[0 for i in range(len(arr))]
            stack=[]
            for i in range(len(arr)):
                while(len(stack) and arr[stack[-1]]>arr[i]):
                    stack.pop()
                if(len(stack)):
                    pse[i] = stack[-1]
                else:
                    pse[i] = -1
                stack.append(i)
            return pse
        nse = findNSE(arr)
        pse = findPSEE(arr)
        total = 0
        mod = (10**9)+7
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total = (total+(right*left*arr[i])%mod)%mod
        return total
