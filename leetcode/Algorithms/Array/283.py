__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""
通过双指针，分别从数组起始位置和最后位置同时向中部扫描，发现0则添加的最后，更新扫描位置下标
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] == 0:
                nums.pop(start)
                nums.append(0)
                end -= 1
            else:
                start += 1
            if nums[end] == 0:
                nums.pop(end)
                nums.append(0)
            end -= 1