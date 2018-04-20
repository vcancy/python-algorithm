__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-
"""

分析：
给的r 和 c 能不能用来塑造一个2d array。比较一下总数就可以了。

遍历二维数组，每c个数值添加到一个1维数组中，再将这个1维数组添加到数组中。

"""

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        index = 0
        temp = []
        res = []
        if len(nums) * len(nums[0]) != r * c:
            return nums

        for i in nums:
            for j in i:
                if index < c:
                    temp.append(j)
                    index += 1
                if index==c:
                    res.append(temp)
                    temp = []
                    index = 0
        return res