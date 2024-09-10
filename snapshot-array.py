class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        self.snap_id=0
    def set(self, index: int, val: int) -> None:
        if(index not in self.arr):
            self.arr[index] = {}
            if(self.snap_id not in self.arr[index]):
                self.arr[index][self.snap_id]= val
            else:
                self.arr[index][self.snap_id] = val
        else:
            self.arr[index][self.snap_id] = val 
    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1
    def get(self, index: int, snap_id: int) -> int:
        if(index not in self.arr):
            return 0
        while snap_id>=0:
            if(snap_id in self.arr[index]):
                return self.arr[index][snap_id]
            snap_id-=1
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
