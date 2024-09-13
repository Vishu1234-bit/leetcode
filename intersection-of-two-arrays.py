class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1len = len(nums1)
        nums2len = len(nums2)
        if(nums1len<nums2len):
            commonlen = nums1len
        else:
            commonlen = nums2len
        result = []
        if(commonlen == nums1len):
            for i in nums1:
                if(i in nums2):
                    if(i not in result):
                        result.append(i)
        else:
            for i in nums2:
                if(i in nums1):
                    if(i not in result):
                        result.append(i)
        return result
                
