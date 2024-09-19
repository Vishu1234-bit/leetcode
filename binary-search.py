class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums)==1):
            return 0 if (nums[0]==target) else -1
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            print(mid)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                high = mid-1
            else:
                low = mid+1   
        return -1     
