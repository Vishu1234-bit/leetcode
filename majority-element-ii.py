class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1=0
        cnt2=0
        el1 = float('-inf')
        el2 = float('-inf')
        for i in range(0,len(nums)):
            if(cnt1==0 and el2!=nums[i]):
                el1 = nums[i]
                cnt1+=1
            elif(cnt2==0 and el1!=nums[i]):
                el2 = nums[i]
                cnt2+=1
            elif(nums[i]==el1):
                cnt1+=1
            elif(nums[i]==el2):
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        checkCnt1=0
        checkCnt2=0
        for i in range(0,len(nums)):
            if(nums[i]==el1):
                checkCnt1+=1
            if(nums[i]==el2):
                checkCnt2+=1
        majority = (len(nums)//3)+1
        res=[]
        if(checkCnt1>=majority):
            res.append(el1)
        if(checkCnt2>=majority):
            res.append(el2)
        return res
