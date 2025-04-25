# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def isLeaf(node):
            if(not node.left and not node.right):
                return True
            return False
        def addLeftBoundary(node,res):
            while(node):
                if(not isLeaf(node)):
                    res.append(node.val)
                if(node.left):
                    node = node.left
                else:
                    node = node.right
        def addLeaves(node,res):
            if(isLeaf(node)):
                res.append(node.val)
            if(node.left):
                addLeaves(node.left,res)
            if(node.right):
                addLeaves(node.right,res)
        def addRightBoundary(node,res):
            tmp = []
            while(node):
                if(not isLeaf(node)):
                    tmp.append(node.val)
                if(node.right):
                    node = node.right
                else:
                    node = node.left
            res.extend(tmp[::-1])
        if(not root):
            return []
        res=[]
        if(not isLeaf(root)):
            res.append(root.val)
        addLeftBoundary(root.left,res)
        addLeaves(root,res)
        addRightBoundary(root.right,res)
        return res
        
