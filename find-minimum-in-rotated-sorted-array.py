class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mini =float('inf')
        while(l<=r):
            m= (l+r)//2
            if(nums[l]<nums[r]):
                mini=min(nums[l],mini)
                break
            elif(nums[l]<=nums[m]):
                mini = min(nums[l],mini)
                l=m+1
            else:
                mini=min(nums[m],mini)
                r=m-1
        return mini
        
