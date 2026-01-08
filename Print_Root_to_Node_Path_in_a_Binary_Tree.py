# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def allRootToLeaf(self, root):
        #your code goes here
		result=[]
		def dfs(root,path):
			if(root is None):
				return 
			path.append(root.data)
			if(root.left is None and root.right is None):
				result.append(path[:])
			else:
				dfs(root.left,path)
				dfs(root.right,path)
			path.pop()
		dfs(root,[])
		return result
