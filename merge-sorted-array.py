class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1ptr = m-1
        nums2ptr = n-1
        ptr = m+n-1
        while(nums2ptr>=0):
            if(nums1ptr>=0 and nums1[nums1ptr]>nums2[nums2ptr]):
                nums1[ptr] = nums1[nums1ptr]
                nums1ptr-=1
            else:
                nums1[ptr]=nums2[nums2ptr]
                nums2ptr-=1
            ptr-=1
