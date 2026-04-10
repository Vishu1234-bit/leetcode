class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashtable = {}
        for i in range(0,len(nums)):
            if(nums[i] in hashtable):
                hashtable[nums[i]].append(i)
            else:
                hashtable[nums[i]]=[i]
        print(hashtable)
        res = float('inf')
        for ele in hashtable:
            indices = hashtable[ele]
            for i in range(len(indices)-2):
                res = min(2*(indices[i+2]-indices[i]),res)
        return res if(res!=float('inf')) else -1
        
            

        
