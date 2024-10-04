# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(l1,l2):
            dummy = ListNode(0)
            current=dummy
            while(l1 and l2):
                if(l1.val<l2.val):
                    current.next = l1
                    l1=l1.next
                else:
                    current.next=l2
                    l2=l2.next
                current=current.next
            if(l1):
                current.next = l1
            if(l2):
                current.next = l2
            return dummy.next
        if(len(lists)==0):
            return None
        n = len(lists)
        
        while(n>1):
            mergedLists = []
            for i in range(0,n,2):
                l1 = lists[i]
                l2 = lists[i+1] if(i+1<n)else None
                mergedLists.append(merge(l1,l2))
            lists = mergedLists
            n = len(lists)
        return lists[0]
