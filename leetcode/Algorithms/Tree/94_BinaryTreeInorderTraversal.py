# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		ret = []
		stack = []
		cur = root
		if not root:
			return ret
		while stack or cur:
			while cur:
				stack.append(cur)
				cur = cur.left
			if not cur:
				node = stack.pop()
				ret.append(node.val)
				cur = node.right

		return ret


if __name__=="__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t2.left = TreeNode(3)
    t1.right = t2
    print(Solution().inorderTraversal(t1))