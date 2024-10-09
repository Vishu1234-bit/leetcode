# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(left,right):
            dummy = ListNode(0)
            temp =dummy
            while(left and right):
                if(left.val<=right.val):
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp=temp.next
            if(left):
                temp.next=left
            if(right):
                temp.next=right
            return dummy.next
        def findMiddleOftheList(ll):
            if(not ll or not ll.next):
                return ll
            slow=ll
            fast = ll.next
            while(fast and fast.next):
                slow=slow.next
                fast=fast.next.next
            return slow
        if(not head or not head.next):
            return head
        ll = head
        middle =findMiddleOftheList(ll)
        right = middle.next
        middle.next=None
        left = ll
        left=self.sortList(left)
        right=self.sortList(right)
        mergedList = merge(left,right)
        return mergedList
