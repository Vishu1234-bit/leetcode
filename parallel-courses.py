from collections import deque,defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = {i:0 for i in range(1,n+1)}
        for prevCourse,nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse]+=1
        queue = deque([courses for courses in range(1,n+1) if in_degree[courses]==0])
        semesters = {i:1 for i in queue}
        topo_order = []
        max_semester = 1
        while(queue):
            node = queue.popleft()
            topo_order.append(node)
            for neighbour in graph[node]:
                in_degree[neighbour]-=1
                if(in_degree[neighbour]==0):
                    queue.append(neighbour)
                    semesters[neighbour] = semesters[node]+1
                    max_semester = max(max_semester,semesters[neighbour])
        if(len(topo_order)<n):
            return -1
        else:
            return max_semester
