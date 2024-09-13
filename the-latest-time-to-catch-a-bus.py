class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        sortedBuses = sorted(buses)
        sortedPassengers = sorted(passengers)
        passengerPtr = 0
        latestTime = -1
        
        for bus in sortedBuses:
            currentCapacity=0
            while(passengerPtr<len(passengers) and sortedPassengers[passengerPtr]<=bus and currentCapacity<capacity):
                passengerPtr+=1
                currentCapacity+=1
        latestTime = sortedPassengers[passengerPtr-1]
        if(currentCapacity != capacity):
            latestTime = sortedBuses[-1]
        while latestTime in sortedPassengers:
            latestTime-=1
        return latestTime
