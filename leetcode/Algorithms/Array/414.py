__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""
要求时间复杂度为n，在最多一次遍历结束后就找到这个第三大的值。
直接设置三个变量来存储遍历过程中所遇到的第一、二、三大的值。
"""
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = None, None, None
        for i in nums:
            if max1 == i or max2 == i or max3 == i:#忽略相同的值
                continue
            if not max1 or i > max1:
                max1, max2, max3 = i, max1, max2
            elif not max2 or i > max2:
                max2, max3 = i, max2
            elif not max3 or i > max3:
                max3 = i

        return max1 if max3 == None else max3