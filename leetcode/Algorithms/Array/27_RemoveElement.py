__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-

"""
通过两个指针i,j
i:新的数组下标，起始为0
j:遍历原数组
当出现不需要删除的数(nums[j]!=val),指针i指向该数，i移动到下一个
最后i为新的数组的长度
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
