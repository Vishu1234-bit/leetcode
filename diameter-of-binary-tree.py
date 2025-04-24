# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if(not node):
                return 0
            left=helper(node.left)
            print("left",left)
            right = helper(node.right)
            print("right",right)
            self.diameter = max(self.diameter,left+right)
            return 1+max(left,right)
        self.diameter=0
        helper(root)
        return self.diameter
