# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node,arr):
            if(node and node.left):
                helper(node.left,arr)
            if(node and node.right):
                helper(node.right,arr)
            if(node):
                arr.append(node.val)
            return
        arr=[]
        helper(root,arr)
        return arr
