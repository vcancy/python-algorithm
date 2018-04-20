# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		ret = []
		if not root:
			return ret
		stack = [root]
		while stack:
			node = stack.pop()
			ret.insert(0, node.val)

			if node.left:
				stack.append(node.left)

			if node.right:
				stack.append(node.right)

		return ret