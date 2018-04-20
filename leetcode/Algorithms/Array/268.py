__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""
数学：
前n项和公式a1*n+n*(n-1)/2,减去nums里面的所有数即是缺失的数
"""
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)+1
        total = n*(n-1)/2
        for i in nums:
            total -=i
        return int(total)