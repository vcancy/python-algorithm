__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""
分析：
使用哈希表保存数组中的数字出现的次数：
当k为0的时候，只需要数字出现次数大于2的全部符合，
否则判断数字+k的值是否在d中出现，出现一次就累加一次
"""

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        cnt = 0
        d = dict()
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if k == 0:
                if d[i] >= 2:
                    cnt += 1
            else:
                if i + k in d.keys():
                    cnt += 1
        return cnt
