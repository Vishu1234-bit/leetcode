class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(node,visited_array,adj_list):
            visited_array[node] = 1
            for neighbour in adj_list[node]:
                if(not visited_array[neighbour]):
                   dfs(neighbour,visited_array,adj_list)
        adj_list={i:[] for i in range(n)}
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited_array = [0 for i in range(n)]
        count=0
        for i in range(n):
            if(not visited_array[i]):
                count+=1
                dfs(i,visited_array,adj_list)
                print(visited_array,count)
        return count
                
