__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：需要找到无序连续子数组的起始位置和结束位置

起始位置：从右到左找到比前面的最小值还大的数

结束位置：从左到右找到比前面的最大值还小的数

eg. [1,3,2,4,5]
起始位置从5开始，直到3，比前面的最小值2还大了，起始位置就是它.
结束位置从1开始，直到2，比前面的最大值3还小了，结束位置就是它.

"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0

        mi = nums[-1]
        ma = nums[0]
        n = len(nums)
        for i in range(n):
            mi = min(mi, nums[n - 1 - i])
            ma = max(ma, nums[i])

            if mi < nums[n - 1 - i]: # 从右到左找到比前面的最小值还大的数
                start = n - 1 - i
            if ma > nums[i]: # 结束位置：从左到右找到比前面的最大值还小的数
                end = i
        if start == 0 and end == 0:
            return 0
        else:
            return end - start + 1
