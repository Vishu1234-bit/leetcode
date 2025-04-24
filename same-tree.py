# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkIdentical(p,q):
            if(not p and not q):
                return True
            if((p and q and p.val!=q.val) or (not p and q) or (not q and p)):
                return False
            elif(p and q and p.val==q.val):
                leftIdentical = checkIdentical(p.left,q.left)
                print(leftIdentical)
                rightIdentical = checkIdentical(p.right,q.right)
                print(rightIdentical)
                return leftIdentical and rightIdentical
        return checkIdentical(p,q)

        
