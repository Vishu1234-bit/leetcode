class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def check(dist):
            countStations = 0
            for i in range(0,len(stations)-1):
                stationInBtw = (stations[i+1]-stations[i])//dist
                if((stations[i+1]-stations[i])/dist == (stationInBtw*dist)):
                    stationInBtw-=1
                countStations += stationInBtw
            return countStations
        low =0 
        high = 0
        for i in range(0,len(stations)-1):
            high = max(stations[i+1]-stations[i],high)
        while((high-low)>10**(-6)):
            mid = (low+high)/2.0
            if(check(mid)>k):
                low=mid
            else:
                high = mid
        return high
                
        
