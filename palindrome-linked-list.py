# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseLinkedList(linkedlist):
            prev = None
            current = linkedlist
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        if not head or not head.next:
            return True
        slow,fast = head,head
        while(fast and fast.next):
            slow= slow.next
            fast = fast.next.next
        secondHalf = reverseLinkedList(slow)
        firstHalf = head
        while(secondHalf):
            if(not firstHalf or firstHalf.val!=secondHalf.val):
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True
        
