__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""
分析：先求出数组的总和，遍历数组，记录当前数组之和tmp，然后对于遍历到的位置，

用总和减去当前数字，得到的结果是否是tmp的两倍，

是的话，那么当前位置就是中心索引，返回即可；

否则就将当前数字加到tmp中继续遍历，遍历结束后还没返回，说明没有中心索引，返回-1即可。
"""

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        total = sum(nums)
        :rtype: int
        """
        total = sum(nums)
        tmp = 0
        for i in range(len(nums)):
            if total - nums[i] == 2 * tmp:
                return i
            else:
                tmp += nums[i]
        return -1
