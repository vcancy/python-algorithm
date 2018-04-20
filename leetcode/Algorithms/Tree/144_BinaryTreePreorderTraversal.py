#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively? - see preTraverse_itr
"""
__author__ = 'YuJie'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root:
            ret.append(root.val)
            if root.left:
                ret.extend(self.preorderTraversal(root.left))
            if root.right:
                ret.extend(self.preorderTraversal(root.right))
        return ret

    def preorder_traversal_iter(self, root:TreeNode):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret


if __name__=="__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t2.left = TreeNode(3)
    t1.right = t2
    print(Solution().preorder_traversal_iter(t1))