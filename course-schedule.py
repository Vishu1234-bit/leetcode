class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseSchedule = defaultdict(list)
        in_degree = {i:0 for i in range(numCourses)}
        for u,v in prerequisites:
            courseSchedule[u].append(v)
            in_degree[v]+=1
        courseOrder=[]
        queue = deque([node for node in in_degree if in_degree[node]==0])
        while(queue):
            currentCourse = queue.popleft()
            courseOrder.append(currentCourse)
            for neighbour in courseSchedule[currentCourse]:
                in_degree[neighbour]-=1
                if(in_degree[neighbour]==0):
                    queue.append(neighbour)
        if(len(courseOrder)==numCourses):
            return True
        else:
            return False
                
        
