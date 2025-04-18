class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x:x[0])
        removalCount =0 
        prevend = intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<prevend):
                removalCount+=1
                prevend = min(prevend,intervals[i][1])
            else:
                prevend = intervals[i][1]
        return removalCount
    

