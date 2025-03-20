class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesserThanPivot = []
        greaterThanPivot = []
        for ele in nums:
            if(ele<pivot):
                lesserThanPivot.append(ele)
            elif(ele>pivot):
                greaterThanPivot.append(ele)
        pivotEquate = [pivot]*(len(nums)-(len(lesserThanPivot)+len(greaterThanPivot)))
        resultNums = lesserThanPivot+pivotEquate+greaterThanPivot
        return resultNums



        
