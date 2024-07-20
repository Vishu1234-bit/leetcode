class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<len(nums) and right>=0):
            if(nums[left]==target):
                return left
            elif(nums[left]>target):
                if(nums[right]==target):
                    return right
                elif(nums[right]<target):
                    return -1
                else:
                    right-=1
            else:
                left+=1
        return -1
