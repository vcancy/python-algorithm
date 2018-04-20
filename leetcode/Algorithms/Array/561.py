__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""
贪婪算法:
要最大化每对中的较小值之和，那么肯定是每对中两个数字大小越接近越好，
因为如果差距过大，而我们只取较小的数字，那么大数字就浪费掉了。
明白了这一点，我们只需要给数组排个序，然后按顺序的每两个就是一对，
我们取出每对中的第一个数即为较小值累加起来即可
"""
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total
