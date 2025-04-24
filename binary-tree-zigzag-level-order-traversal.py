# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        result = []
        queue = deque([root])
        ltor = True
        while(queue):
            level=[]
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                level.append(curr_node.val)
                if(curr_node.left):
                    queue.append(curr_node.left)
                if(curr_node.right):
                    queue.append(curr_node.right)
            if(not ltor):
                level = level[::-1]
            result.append(level)
            ltor = not ltor
        return result
