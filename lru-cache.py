from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.lruQueue = deque()
    def get(self, key: int) -> int:
        if(key in self.lru):
            if(key in self.lruQueue):
                self.lruQueue.remove(key)
            self.lruQueue.append(key)
            return self.lru[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if(key in self.lru):
            self.lru[key] = value
        else:                                       
            if(len(self.lru)<self.capacity):
                self.lru[key] = value
            else:
                del self.lru[self.lruQueue.popleft()]
                self.lru[key]=value
        if(key in self.lruQueue):
                self.lruQueue.remove(key)
        self.lruQueue.append(key)
        
                
               


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
