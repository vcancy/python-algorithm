__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：
查找数组中的最大元素是否至少是数组中每个其他数字的两倍，

设置临时变量保存数组最大值与第二大值，当最大值大于第二大值的两倍即满足，

否则不满足条件

"""


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, index = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
                index = i
            elif nums[i] > second:
                second = nums[i]

        return index if (second == 0 or first / second >= 2) else -1
