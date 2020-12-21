# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode,carry=0) -> ListNode:
        while(l1 is not None or l2 is not None):
            fdata = 0 if l1 is None else l1.val
            sdata = 0 if l2 is None else l2.val
            Sum = carry + fdata + sdata
            carry = 1 if Sum>=10 else 0
            Sum = Sum if Sum<10 else Sum%10
            temp = ListNode(Sum)
            if(l1.next!= None or l2.next!=None or carry!=0):
                if l1.next == None:
                    l1.next =ListNode(0)
                if l2.next == None:
                    l2.next = ListNode(0)
                temp.next = self.addTwoNumbers(l1.next,l2.next,carry)
            return temp
