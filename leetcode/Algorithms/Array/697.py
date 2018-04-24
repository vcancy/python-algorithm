__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：假设数组的度为d，那么肯定有一个元素x出现了d次。

要使子数组的度也为d，同样的元素在子数组也出现d次，同时首位的元素都为x。

假设left为左边第一个出现的元素，right为右边第一个出现的元素，

那么元素出现的次数就为right[x] - left[x] + 1。选择最小即结果

"""


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}  # 分别保存左侧第一次出现，右侧第一次出现，每个元素出现的总次数
        for i, v in enumerate(nums):
            if v not in left.keys():  # 发现有元素已经出现过，重置左侧元素位置
                left[v] = i
            right[v] = i
            count[v] = count.get(v, 0) + 1

        degree = max(count.values())  # 求元素最大出现次数
        ret = len(nums)
        for k, v in count.items():
            if v == degree:
                ret = min(ret, right[k] - left[k] + 1)
        return ret
