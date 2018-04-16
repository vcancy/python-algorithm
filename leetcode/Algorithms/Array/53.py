__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""
遍历数组，当从头到尾部遍历数组遇到一个数有两种选择 
（1）加上这个数后数值变大：继续加后面的数 

（2）加上这个数后数值变小：从当前开始重新加后面的数

考察DP：https://blog.csdn.net/baidu_28312631/article/details/47418773
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            sum = max(sum + nums[i], nums[i])
            max_sum = max(sum, max_sum)
        return max_sum

# TODO DP时间复杂度O(n). 可使用分治法求解