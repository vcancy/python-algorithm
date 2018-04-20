# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		ret = []
		if not root:
			return ret
		stack = [root]
		while stack:
			lev = []
			temp = []
			for node in stack:
				lev.append(node.val)
				if node.left:
					temp.append(node.left)
				if node.right:
					temp.append(node.right)

			stack = temp
			ret.append(lev)
		return ret

