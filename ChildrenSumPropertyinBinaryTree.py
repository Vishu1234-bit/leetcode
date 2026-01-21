class Solution:
    def checkChildrenSum(self, root: TreeNode) -> bool:
        # Your code goes here
        if(root is None):
            return True
        if(root.left is None and root.right is None):
            return True
        left = root.left.val if root.left else 0
        right = root.right.val if root.right else 0
        if(root.val != left+right):
            return False
        return (self.checkChildrenSum(root.left) and
        self.checkChildrenSum(root.right))
