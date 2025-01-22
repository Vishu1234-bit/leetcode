class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.minfreq =0
        self.freq = {}
        self.freqkey= defaultdict(OrderedDict)
        self.lfu = {}
    def updateFreq(self,key):
        frequency = self.freq[key]
        del self.freqkey[frequency][key]
        if(not self.freqkey[frequency]):
            del self.freqkey[frequency]
            if(frequency==self.minfreq):
                self.minfreq+=1
        self.freq[key]+=1
        frequency = self.freq[key]
        self.freqkey[frequency][key] = True
    def get(self, key: int) -> int:
        if(key in self.lfu):
            self.updateFreq(key)
            return self.lfu[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.lfu):
            self.lfu[key]=value
            self.updateFreq(key)
        else:
            if(len(self.lfu)>=self.capacity):
                lfuKey,_ = self.freqkey[self.minfreq].popitem(last=False)
                del self.freq[lfuKey]
                del self.lfu[lfuKey]
                
            self.lfu[key]=value
            self.freq[key]=1
            self.minfreq=1
            self.freqkey[1][key]=True
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
