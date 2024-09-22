class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def makeJump(sorted_indices):
            n = len(sorted_indices)
            result = [None]*n
            stack = []
            for i in sorted_indices:
                while stack and stack[-1]<i:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        oddBool = [False for i in range(len(arr))]
        evenBool = [False for i in range(len(arr))]
        n = len(arr)
        if(n==1):
            return 1
        oddBool[n-1] = True
        evenBool[n-1] = True
        sorted_indices = sorted(range(n), key=lambda i:(arr[i],i))
        next_higher = makeJump(sorted_indices)
        print(next_higher)
        sorted_indices = sorted(range(n), key=lambda i:(-arr[i],i))
        next_lower = makeJump(sorted_indices)
        print(next_lower)
        for idx in range(n-2,-1,-1):
            if(next_higher[idx] is not None):
                oddBool[idx] = evenBool[next_higher[idx]]
                print("oddBool",oddBool)
            if(next_lower[idx] is not None):
                evenBool[idx] = oddBool[next_lower[idx]]
                print("evenBool",evenBool)
        return sum(oddBool)
