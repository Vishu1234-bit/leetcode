class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(low,mid,high):
            left=low
            right=mid+1
            cnt=0
            temp=[]
            while(left<=mid and right<=high):
                if(nums[left]>(2*nums[right])):
                    cnt+=(mid-left+1)
                    right+=1
                else:
                    left+=1
            left=low
            right=mid+1
            while(left<=mid and right<=high):
                if(nums[left]<=nums[right]):
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while(left<=mid):
                temp.append(nums[left])
                left+=1
            while(right<=high):
                temp.append(nums[right])
                right+=1
            for i in range(len(temp)):
                nums[low+i] = temp[i]
            return cnt
        def mergeSort(low,high):
            cnt=0
            if(low<high):
                mid=(low+high)//2
                cnt+=mergeSort(low,mid)
                cnt+=mergeSort(mid+1,high)
                cnt+=merge(low,mid,high)
            return cnt
        return mergeSort(0,len(nums)-1)
