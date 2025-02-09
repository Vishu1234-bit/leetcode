class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(edges,nodeStart):
            n = len(edges)
            dist = [-1 for i in range(n)]
            que = deque([nodeStart])
            dist[nodeStart]=0
            while(que):
                curr_node = que.popleft()
                next_node = edges[curr_node]
                if(next_node!=-1 and dist[next_node]==-1):
                    dist[next_node]=dist[curr_node]+1
                    que.append(next_node)
            return dist

        n = len(edges)
        dist1 = bfs(edges,node1)
        dist2 = bfs(edges,node2)
        minMaxDist = float('inf')
        result=-1
        for i in range(n):
            if(dist1[i]!=-1 and dist2[i]!=-1):
                maxDist = max(dist1[i],dist2[i])
                if(maxDist<minMaxDist):
                    minMaxDist=maxDist
                    result=i
                elif(maxDist == minMaxDist):
                    result = min(result,i)
        return result
            
