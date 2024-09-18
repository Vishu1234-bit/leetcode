class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def union(arr1,arr2):
            for i in arr2:
                if i not in arr1:
                    arr1.append(i)
            return arr1
        logs = sorted(logs,key=lambda x:x[0])
        frndsgrp = [[i] for i in range(n)]
        print(frndsgrp)
        for log in logs:
            timestamp,a,b = log[0],log[1],log[2]
            for frnds in frndsgrp:
                if(a in frnds):
                    frndsSet1 = frnds
                if(b in frnds):
                    frndsSet2 = frnds
            if(frndsSet1!=frndsSet2):
                unionFrnds = union(frndsSet1,frndsSet2)
                frndsgrp.remove(frndsSet1)
                frndsgrp.remove(frndsSet2)
                frndsgrp.append(unionFrnds)
            if(len(frndsgrp)==1):
                return timestamp
        return -1
        
