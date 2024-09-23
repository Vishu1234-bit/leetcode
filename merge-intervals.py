class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)==1):
            return intervals
        intervals = sorted(intervals,key=lambda x:x[0])
        mergedIntervals=[]
        print(intervals)
        for idx in range(1,len(intervals)):
            start,end = intervals[idx][0],intervals[idx][1]
            if(len(mergedIntervals)>=1 and mergedIntervals[-1][1]>=start):
                lastInterval = mergedIntervals.pop()
                mergedIntervals.append([min(lastInterval[0],start),max(lastInterval[1],end)])
            elif(intervals[idx-1][1]>=start):
                mergedIntervals.append([intervals[idx-1][0],max(intervals[idx-1][1],end)])
            else:
                if(idx==1):
                    mergedIntervals.append(intervals[idx-1])
                mergedIntervals.append(intervals[idx])
        return mergedIntervals

        
