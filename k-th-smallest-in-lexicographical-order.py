class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countPrefix(curr,n):
            count=0
            next_curr=curr+1
            while(curr<=n):
                count+=min(n+1,next_curr)-curr
                curr*=10
                next_curr*=10
            return count
        curr=1
        k-=1
        while(k>0):
            steps = countPrefix(curr,n)
            if(steps<=k):
                curr+=1
                k-=steps
            else:
                curr*=10
                k-=1
        return curr
