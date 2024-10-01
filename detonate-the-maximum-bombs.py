class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def can_trigger(i,j):
            x1,y1,r1 = bombs[i] 
            x2,y2,r2 = bombs[j]
            return ((x1-x2)**2 + (y1-y2)**2)**(1/2) <=r1
        def dfs(i,visited):
            visited.add(i)
            count=1
            for neighbour in graph[i]:
                if(neighbour not in visited):
                    count+=dfs(neighbour,visited)
            return count
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if(i!=j and can_trigger(i,j)):
                    graph[i].append(j)
        maximumDetonation = 0
        for i in range(n):
            visited=set()
            maximumDetonation = max(maximumDetonation,dfs(i,visited))
        return maximumDetonation


        
