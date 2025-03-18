from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseSchedule = defaultdict(list)
        in_degree = {i:0 for i in range(numCourses)}
        for u,v in prerequisites:
            courseSchedule[v].append(u)
            in_degree[u]+=1
        queue = deque([node for node in in_degree if in_degree[node]==0])
        courseOrder=[]
        while(queue):
            currentCourse = queue.popleft()
            courseOrder.append(currentCourse)
            for neighbours in courseSchedule[currentCourse]:
                in_degree[neighbours]-=1
                if(in_degree[neighbours]==0):
                    queue.append(neighbours)
        return courseOrder if(len(courseOrder)==numCourses) else []
                 
