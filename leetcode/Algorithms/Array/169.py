__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-

"""
摩尔投票：
每次从序列里选择两个不相同的数字删除掉（或称为“抵消”）
最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个。
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            if count == 0:
                record = nums[i]
                count += 1
            elif record == nums[i]:
                count += 1
            else:
                count -= 1
        return record
