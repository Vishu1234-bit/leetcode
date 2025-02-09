class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False for i in range(len(edges))]
        timestamp = [-1 for i in range(len(edges))]
        maxCycleLen = -1
        def dfs(node,time):
            nonlocal maxCycleLen
            if(visited[node] or node==-1):
                return 
            if(timestamp[node]!=-1):
                maxCycleLen = max(maxCycleLen,time-timestamp[node])
                return
            timestamp[node] = time
            dfs(edges[node],time+1)
            visited[node]=True
        for i in range(len(edges)):
            if(not visited[i]):
                dfs(i,0)
        return maxCycleLen
