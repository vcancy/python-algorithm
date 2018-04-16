__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""
分析：
题目中要求将nums2插入nums1中，最后存在nums1中
最后新的nums1的大小为m+n-1
倒序nums1和nums2，判断最后一位，越大的数放在新nums1的最后
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m = m - 1
        n = n - 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
