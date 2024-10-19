from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def dfs(node,parent,visited):
		    visited[node]=True
		    for neighbour in adj[node]:
		        if(not visited[neighbour]):
		            if(dfs(neighbour,node,visited)):
		                return True
		        elif(neighbour!=parent):
		            return True
		    return False
		        
		    
		visited = [False for i in range(V)]
		for i in range(V):
		    if(not visited[i]):
		        if(dfs(i,-1,visited)):
		            return True
		return False
