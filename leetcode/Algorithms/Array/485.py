__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""

设定一个计数器，表示连续1的个数，当遇到0，清空计数器

另外一个变量存结果数据，遇到1，与计数器比较取最大值

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, res=0,0
        for i in nums:
            if i ==1:
                res = max(res,cnt+1)
                cnt+=1
            else:
                cnt=0
        return res