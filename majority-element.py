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

//O(1) Space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count=0
        for i in nums:
            if(count==0):
                candidate = i
                count+=1
            elif(candidate==i):
                count+=1
            else:
                count-=1
        return candidate
            

        
