class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node,visited):
            visited[node]=True
            for edge in range(len(isConnected)):
                if(isConnected[node][edge] == 1 and not visited[edge]):
                    dfs(edge,visited)
        visited = [False for i in range(len(isConnected))]
        provinceCount=0
        for node in range(len(isConnected)):
            if(not visited[node]):
                provinceCount+=1
                dfs(node,visited)
        return provinceCount
