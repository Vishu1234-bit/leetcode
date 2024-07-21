# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr_node = dummy
        first = curr_node.next
        if(first):
            second = first.next
        else:
            return head
        while(first and second):
            first.next = second.next
            second.next = first
            curr_node.next = second
            curr_node = first
            first = curr_node.next
            if(first):
                second = first.next
        return dummy.next
