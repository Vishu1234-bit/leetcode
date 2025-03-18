from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left=0
        right=0
        maxQueue = deque()
        minQueue = deque()
        maxlength=0
        while(right<len(nums)):
            while(maxQueue and nums[right]>maxQueue[-1]):
                maxQueue.pop()
            maxQueue.append(nums[right])
            while(minQueue and nums[right]<minQueue[-1]):
                minQueue.pop()
            minQueue.append(nums[right])
            if(maxQueue[0]-minQueue[0]>limit):
                if(nums[left]==maxQueue[0]):
                    maxQueue.popleft()
                if(nums[left]==minQueue[0]):
                    minQueue.popleft()
                left+=1
            maxlength = max(maxlength,right-left+1)
            right+=1
        return maxlength
