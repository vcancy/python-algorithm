__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-
"""

一个重要条件就是1 ≤ a[i] ≤ n (n = size of array)，

意味着数组里面的每一个值都可以映射到数组的下标中

比如[4,3,2,7,8,2,3,1]:

4-对应数组的下标3

3-对应数组的下标2

...

遍历数组，获取数组值对应的下标，然后设置该下标对应的值为当前值的取反(数值大于0时，因为可能有重复数据)

接下来再次遍历数组，若数值>0，那么表示该下标的值未被修改，即下标+1的值就为查找的确实数字


"""
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i, v in enumerate(nums):
            if v > 0:
                ret.append(i + 1)
        return ret
