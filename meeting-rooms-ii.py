import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = sorted([i[0] for i in intervals])
        endTimes = sorted([i[1] for i in intervals])
        startPtr,endPtr = 0,0
        rooms = 0
        max_rooms=0
        while(startPtr<len(intervals)):
            if(startTimes[startPtr]<endTimes[endPtr]):
                rooms+=1
                startPtr+=1
            else:
                rooms-=1
                endPtr+=1
            max_rooms = max(rooms,max_rooms)
        return max_rooms

