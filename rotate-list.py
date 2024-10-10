# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def findLengthOfLL(head):
            count=0
            while(head):
                count+=1
                head=head.next
            return count
        length = findLengthOfLL(head)
        if(length):
            k = k%length
        if(not head or not head.next or k==0):
            return head
        first =head
        second=head
        for i in range(k):
            first = first.next
        while(first and first.next):
            second = second.next
            first = first.next
        dummy = second.next
        second.next = None
        first.next = head
        
        return dummy
