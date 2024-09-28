# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry = 0) -> Optional[ListNode]:
        if(l1 is None and l2 is None and carry==0):
            return  None
        firstVal = 0 if l1 is None else l1.val
        secondVal = 0 if l2 is None else l2.val
        sumOf2nodes = firstVal+secondVal+carry
        carry = sumOf2nodes//10
        dummy= ListNode(sumOf2nodes%10)
        nextl1 = l1.next if l1 else None
        nextl2 = l2.next if l2 else None
        dummy.next = self.addTwoNumbers(nextl1,nextl2,carry)
        return dummy

