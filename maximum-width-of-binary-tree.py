# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if(not root):
            return 0
        maxWidth=0
        queue = deque([(root,0)])
        while(queue):
            levelLength = len(queue)
            _,first_index  = queue[0]
            for i in range(levelLength):
                node,index = queue.popleft()
                index-=first_index
                if(node.left):
                    queue.append((node.left,2*index))
                if(node.right):
                    queue.append((node.right,2*index+1))
                if(i==levelLength-1):
                    maxWidth = max(maxWidth,index+1)
        return maxWidth
