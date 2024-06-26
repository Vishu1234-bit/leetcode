class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_product =1
        total_product_without_zero=1
        zero_count=0
        for i in nums:
            total_product*=i
            if(i!=0):
                total_product_without_zero*=i
            else:
                zero_count+=1
        answer=[]
        for i in nums:
            if(i==0 and zero_count==1):
               answer.append(total_product_without_zero)
            elif(i==0 and total_product==0):
                answer.append(0)
            else:
               answer.append(total_product//i)
        return answer
