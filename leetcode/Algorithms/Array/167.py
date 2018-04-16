__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-

"""
因为有序，所以可以采用二分法，首位相加和目标值判断：
1。大于目标值，移动尾部到前一个
2。小于目标值，移动首部到下一个
3。相等返回，要求索引从1开始，所以返回的是得到的位置加1

"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers) - 1
        while low < high:
            tmp = numbers[low] + numbers[high]
            if tmp == target:
                return [low + 1, high + 1]
            elif tmp > target:
                high -= 1
            else:
                low += 1
