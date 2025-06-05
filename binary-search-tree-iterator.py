# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack  = []
        self.inorder(root)
        self.pointer=-1
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            self.stack.append(root.val)
            self.inorder(root.right)
    def next(self) -> int:
        self.pointer+=1
        if(self.pointer<len(self.stack)):
            return self.stack[self.pointer]
        return null
    def hasNext(self) -> bool:
        return self.pointer+1<len(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
