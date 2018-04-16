__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-

"""
主要考察二分搜索，当未找到时直接返回最后一次判断的数组位置即可
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            guess = nums[mid]
            if target > guess:
                low = mid + 1
            elif target < guess:
                high = mid
            else:
                return mid
        return low #未找到target最后一次判断的位置就是插入位置
