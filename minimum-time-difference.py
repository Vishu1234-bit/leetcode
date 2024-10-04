class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convertToMinutes(time):
            hours = int(time[:2])
            minutes = int(time[3:])
            return 60*hours+minutes
        timeconverted = sorted([convertToMinutes(time) for time in timePoints])
        minDifference = float('inf')
        for i in range(0,len(timeconverted)-1):
            minDifference = min(minDifference,timeconverted[i+1]-timeconverted[i])
        circularDiff = (1440-timeconverted[-1])+timeconverted[0]
        minDifference = min(minDifference,circularDiff)
        return minDifference
