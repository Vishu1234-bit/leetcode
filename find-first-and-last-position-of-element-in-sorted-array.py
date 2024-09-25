class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums,target,leftBias):
            low=0
            high=len(nums)-1
            targetIndex=-1
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    targetIndex=mid
                    if(leftBias):
                        high = mid-1
                    else:
                        low = mid+1
                elif(nums[mid]>target):
                    high=mid-1
                else:
                    low=mid+1
            return targetIndex
        left = binSearch(nums,target,True)
        right = binSearch(nums,target,False)
        return [left,right]
        
