import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enqueue,process,i) for i,(enqueue,process) in enumerate(tasks)]
        tasks.sort()
        result=[]
        minHeap=[]
        i=0
        time=0
        n = len(tasks)
        while(i<n or minHeap):
            while(i<n and tasks[i][0]<=time):
                enqueue,process,ind = tasks[i]
                heapq.heappush(minHeap,(process,ind))
                i+=1
            if(not minHeap):
                time = tasks[i][0]
                continue
            process,ind = heapq.heappop(minHeap)
            result.append(ind)
            time+=process
        return result


