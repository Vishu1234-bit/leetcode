class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=set()
        n,p,z = [],[],[]
        for num in nums:
            if(num<0):
                n.append(num)
            elif(num>0):
                p.append(num)
            else:
                z.append(num)
        if(len(z)>=3):
            res.add((0,0,0))
        N,P=set(n),set(p)
        if z:
            for i in P:
                if((-1*i) in N):
                    res.add((-1*i,0,i))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                sum_pair = n[i]+n[j]
                if((-1*sum_pair) in P):
                    res.add(tuple(sorted([n[i],n[j],-1*sum_pair])))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                sum_pair = p[i]+p[j]
                if((-1*sum_pair) in N):
                    res.add(tuple(sorted([p[i],p[j],-1*sum_pair])))
        return res
        
            
