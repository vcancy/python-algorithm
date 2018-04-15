__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-
"""
遍历数组，在哈希表中存数字和索引，找到返回
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for i,num in enumerate(nums):
            v = target-num
            if v in hashtable:
                return [hashtable[v],i]
            else:
                hashtable[num]=i