class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum=[0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        print(prefix_sum)
        def binary_search(nums,target):
            left=0
            right=len(nums)-1
            ans =len(nums)
            while(left<=right):
                mid = (left+right)//2
                if(nums[mid]>=target):
                    ans=mid
                    right = mid-1
                else:
                    left=mid+1
            return ans              
        left=0
        right=len(prefix_sum)-1
        min_len = float('inf')
        for i in range(len(nums)):
            target_sum = prefix_sum[i]+target
            j =binary_search(prefix_sum,target_sum)
            print('j',j,'i',i)
            if(j<len(prefix_sum)):
                min_len = min(min_len,j-i)
                print('min',min_len)
        return min_len if(min_len!=float('inf')) else 0

            
