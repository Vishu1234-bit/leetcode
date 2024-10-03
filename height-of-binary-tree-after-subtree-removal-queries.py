# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        def solve(root,level):
            eulerTour.append((root.val,level))
            if(root.left):
                solve(root.left,level+1)
            if(root.right):
                solve(root.right,level+1)
            eulerTour.append((root.val,level))
        eulerTour=[]
        solve(root,1)
        d={}
        for i,el in enumerate(eulerTour):
            if(el[0] in d):
                d[el[0]].append(i)
            else:
                d[el[0]]=[i]
        pre=[0]
        for node,level in eulerTour:
            pre.append(max(pre[-1],level))
        suff=[0]
        for node,level in eulerTour[::-1]:
            suff.append(max(suff[-1],level))
        suff=suff[::-1]
        res=[]
        for query in queries:
            start,end = d[query]
            res.append(max(pre[start],suff[end+1])-1)
        return res
