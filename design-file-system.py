class FileSystem:

    def __init__(self):
        self.fileDict={}

    def createPath(self, path: str, value: int) -> bool:
        breakInd = len(path)-1
        while(breakInd>=0):
            if(path[breakInd]=="/"):
                break
            breakInd-=1
        print(breakInd,path)
        if(path in self.fileDict or (path[:breakInd] not in self.fileDict and breakInd!=0)):
            return False
        else:
            self.fileDict[path] = value
            return True
    def get(self, path: str) -> int:
        if(path in self.fileDict):
            return self.fileDict[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
