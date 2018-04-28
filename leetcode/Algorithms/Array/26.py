__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：数组为有序的，只需要遍历一次，前后值不相同的移出数组

定义一个临时变量保存最近一次的值，返回最后数组的大小即可

"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = nums[0]
        index = 1
        n = len(nums)
        while index < n:
            if nums[index] == temp:
                nums.pop(index)
                n -= 1
            else:
                temp = nums[index]
                index += 1
        return index
