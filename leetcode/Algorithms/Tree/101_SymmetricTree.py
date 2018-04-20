# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def levelOrder(self, root):
		ret = []
		if not root:
			return ret
		stack = [root]
		while stack:
			lev = []
			temp = []
			for node in stack:
				if node:
					lev.append(node.val)
					temp.append(node.left)
					temp.append(node.right)
				else:
					lev.append(None)

			stack = temp
			ret.append(lev)
		return ret


	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return False
		trees = self.levelOrder(root)
		for level in trees[1:]:
			for index,val in enumerate(level[:int(len(level)/2)]):
				if val!=level[len(level)-1-index]:
					return False
		return True


if __name__=="__main__":
	root = TreeNode(1)
	l1 = TreeNode(2)
	r1 = TreeNode(2)
	l1l = TreeNode(3)
	l1r = TreeNode(4)
	r1l = TreeNode(4)
	r1r = TreeNode(3)
	l1.left = l1l
	l1.right = l1r
	r1.left = r1l
	r1.right = r1r
	root.left = l1
	root.right = r1

	print(Solution().isSymmetric(root))