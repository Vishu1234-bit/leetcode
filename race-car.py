from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set([(0,1)])
        while(queue):
            position, speed,steps = queue.popleft()
            if(position==target):
                return steps
            new_position = position+speed
            new_speed = speed*2
            if((new_position,new_speed) not in visited and abs(new_position)<2*target):
                queue.append((new_position,new_speed,steps+1))
                visited.add((new_position,new_speed))
            new_speed = -1 if speed>0 else 1
            if((position,new_speed) not in visited):
                queue.append((position,new_speed,steps+1))
                visited.add((position,new_speed))
            
