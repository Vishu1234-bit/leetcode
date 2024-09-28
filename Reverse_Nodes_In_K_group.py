# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(temp,k):
            k-=1
            curr = temp
            while(curr is not None and k>0):
                curr = curr.next
                k-=1
            return curr
        def reverseLL(temp):
            prev = None
            curr = temp
            while(curr):
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        dummy = ListNode(0,head)
        groupPrev= None
        temp = head
        while(True):
            kthNode = getKthNode(temp,k)
            if(kthNode==None):
                if(groupPrev):
                    groupPrev.next = temp
                break
            groupNext= kthNode.next
            kthNode.next=None
            newhead = reverseLL(temp)
            print(newhead)
            if(temp==head):
                head  = kthNode
            else:
                groupPrev.next = newhead
            temp.next = groupNext
            groupPrev = temp
            temp = groupNext
            
        return head
        
