class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        index=0
        maxFrequency=0
        majority_ele = nums[0]
        while(index<len(nums)):
            frequency[nums[index]] = frequency.get(nums[index],0)+1
            index+=1
        for i in frequency:
            if(frequency[i]>maxFrequency):
                maxFrequency = frequency[i]
                majority_ele=i
        return majority_ele

        
