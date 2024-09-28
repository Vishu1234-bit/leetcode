# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getKthElement(curr,k):
            k-=1
            temp=curr
            while(temp is not None and k>0):
                temp=temp.next
                k-=1
            return temp
        def swapNodes(curr):
            temp = curr
            prev=None
            nextNode = temp.next
            temp.next = prev
            nextNode.next = temp
            temp=nextNode
            return temp
        if(not head):
            return None
        curr =head
        groupPrev = None
        while(True):
            kthNode = getKthElement(curr,2)
            if(kthNode==None):
                if(groupPrev):
                    groupPrev.next = curr
                break
            groupNxt = kthNode.next
            kthNode.next=None
            newHead = swapNodes(curr)
            if(curr==head):
                head = kthNode
            else:
                groupPrev.next = newHead
            curr.next = groupNxt
            groupPrev = curr
            curr = groupNxt
        return head
