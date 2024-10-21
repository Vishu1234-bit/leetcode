class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequence=[]
        for num in nums:
            left=0
            right=len(sequence)
            while(left<right):
                mid = (left+right)//2
                if(sequence[mid]<num):
                    left=mid+1
                else:
                    right=mid
            print(left,sequence)
            if(left==len(sequence)):
                sequence.append(num)
                print("appending",sequence)
            else:
                sequence[left]=num
                print("changing",sequence)
        return len(sequence)
